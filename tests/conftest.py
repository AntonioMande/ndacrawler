import pytest
from ndacrawler import get_drugs


@pytest.fixture
def drugs():
    return get_drugs()
