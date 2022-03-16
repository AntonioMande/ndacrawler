import pytest
from ndacrawler import get_drugs

# For testing
# Cache for speeding up

import requests_cache

requests_cache.install_cache("demo_cache")


@pytest.fixture
def drugs():
    return get_drugs()


def test_headers(drugs):
    human_drugs = drugs["Human"]
    human_drugs.headers
    human_drugs.data
    human_drugs.to_csv("Test.csv")
    assert True
