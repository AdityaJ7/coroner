import json
import logging
import requests

class Mode:
    NORMAL = 0
    DEBUG = 1

class Spasm:
    """For gathering twitch data"""

    def __init__(self, sec_path, mode=Mode.NORMAL):
        """Reads the secret config file and gets OAuth creds"""
        self._mode = mode
        with open(sec_path, "r") as f:
            cfg = json.load(f)
            self._cid = cfg["client_id"]
            self._csc = cfg["client_secret"]

        self.request_access_token()

    @property
    def cid(self):
        """Accessor for cid"""
        return self._cid

    def request_access_token(self):
        """Requests an access token from twitch"""
        url = "https://id.twitch.tv/oauth2/token"
        form = {
            "client_id": self._cid,
            "client_secret": self._csc,
            "grant_type": "client_credentials"
        }
        req = requests.post(url, data=form)
        self._tkn = req.json()["access_token"]
        self._hdrs = {
            "Client-ID": self._cid,
            "Authorization": "Bearer {}".format(self._tkn)
        }

    def get_game_from_id(self, game_id):
        """Gets the game name from the given id"""
        url = "https://api.twitch.tv/helix/games?id={}".format(game_id)
        data = self.make_request(url)
        name = data["data"][0]["name"]
        logging.debug(name)

        return name

    def get_most_active(self, game_id):
        """Gets the most active streams for the given game id"""
        url = "https://api.twitch.tv/helix/streams?game_id={}".format(game_id)
        data = self.make_request(url)
        titles = [item["title"] for item in data["data"]]
        logging.debug("Titles: {}".format(titles))

        return data

    def make_request(self, url):
        """Makes the specified url request"""
        req = requests.get(url, headers=self._hdrs)
        data = req.json()

        return data
