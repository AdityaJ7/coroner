import json
import logging
import pycurl

class Spasm:
    '''For gathering twitch data'''

    def __init__(self, sec_path):
        with open(sec_path, 'r') as f:
            cfg = json.load(f)
            self.cid_ = cfg["client_id"]

            logging.debug("Client Id: {}".format(self.cid_))

    def get_client_id(self):
        return self.cid_

    def get_active(self):
        '''Gets the most active streams for the given game id'''
        '''
        curl -H 'Client-ID: p0gch4mp101fy451do9uod1s1x9i4a' -X GET 'https://api.twitch.tv/helix/streams?game_id=33214'
        '''

