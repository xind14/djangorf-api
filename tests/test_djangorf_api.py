
import pytest
from djangorf_api.djangorf_api import djangorf_api 


# Demo Tests

@pytest.mark.skip
def test_start():
    actual = djangorf_api()
    expected = "Starter test"
    assert actual == expected

@pytest.mark.skip
def test_fixture_01(fixture_01):
    actual = djangorf_api(fixture_01)
    expected = "Starter fixture"
    assert actual == expected


# Demo Fixture
        
@pytest.fixture 
def fixture_01():
    yield "Starter fixture"

