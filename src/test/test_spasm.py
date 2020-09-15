import json
import logging
from spasm import spasm

def test_client_id():
    """ Simple test case for spasm"""
    with open("../config/secret.json", 'r') as f:
        cid = json.load(f)["client_id"]

    sp = spasm.Spasm("../config/secret.json")

    assert cid == sp.cid

def test_get_active():
    sp = spasm.Spasm("../config/secret.json")
    sp.get_most_active(33214)

def test_get_game_name():
    sp = spasm.Spasm("../config/secret.json")
    gm_nm = sp.get_game_from_id(33214)

    assert gm_nm == "Fortnite"
    
