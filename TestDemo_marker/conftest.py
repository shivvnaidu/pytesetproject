import pytest
@pytest.fixture(scope="module",autouse=True)
def setup():
    print(" open browser")
    print(" login ")
    yield
    print(" logout ")



