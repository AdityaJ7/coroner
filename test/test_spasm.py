import json
import logging
from spasm import spasm

def test_spasm():
    ''' Simple test case for spasm'''
    with open("config/secret.json", 'r') as f:
        sec = json.load(f)["client_id"]

    sp = spasm.Spasm("config/secret.json")

    assert sec == sp.get_client_id()
