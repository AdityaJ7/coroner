import json
import logging
from spasm import spasm

def test_client_id():
    ''' Simple test case for spasm'''
    with open("config/secret.json", 'r') as f:
        cid = json.load(f)["client_id"]

    sp = spasm.Spasm("config/secret.json")

    assert cid == sp.get_client_id()
