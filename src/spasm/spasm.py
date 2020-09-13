import json
import logging
import requests


class Spasm:
    '''For gathering twitch data'''

    def __init__(self, sec_path):
        '''Reads the secret config file and gets OAuth creds''' 
        with open(sec_path, 'r') as f:
            cfg = json.load(f)
            self.cid_ = cfg["client_id"]
            self.csc_ = cfg["client_secret"]

        self.request_access_token()

    def request_access_token(self):
        '''Requests an access token from twitch'''
        url = "https://id.twitch.tv/oauth2/token"
        form = {
            "client_id": self.cid_,
            "client_secret": self.csc_,
            "grant_type": "client_credentials"
        }
        req = requests.post(url, data=form)
        self.tkn_ = req.json()['access_token']
        self.hdrs_ = {
            "Client-ID": self.cid_,
            "Authorization": "Bearer {}".format(self.tkn_)
        }

    def get_game_from_id(self, game_id):
        '''Gets the game name from the given id'''
        url = "https://api.twitch.tv/helix/games?id={}".format(game_id)
        data = self.make_request(url)
        name = data['data'][0]['name']
        logging.debug(name)

        return name

    def get_active(self, game_id):
        '''Gets the most active streams for the given game id'''
        url = "https://api.twitch.tv/helix/streams?game_id={}".format(game_id)
        data = self.make_request(url)
        for item in data["data"]:
            unm = item["user_name"]
            titl = item["title"]

            logging.debug("Game: {}, Username: {}, Title: {}".format(
                self.get_game_from_id(game_id), unm, titl))

        return data

    def make_request(self, url):
        '''Makes the specified url request'''
        req = requests.get(url, headers=self.hdrs_)
        data = req.json()

        return data
