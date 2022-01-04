import pytest
import os

from tests.helpers.triple_store import TripleStore

FIXTURE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'files')

def test_clear():
    ts = TripleStore()
    ts.clear()

def test_load():
    ts = TripleStore()
    ts.upload(os.path.join(FIXTURE_DIR, "org.ttl"))
