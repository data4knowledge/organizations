import pytest

from tests.helpers.triple_store import TripleStore

def test_clear():
    ts = TripleStore()
    ts.clear()

def test_load():
    ts = TripleStore()
    ts.upload("/Users/daveih/Documents/python/organizations/tests/files/org.ttl")
