import sys

import pytest
@pytest.mark.smoke
def test_login():
    print("login details")
@pytest.mark.regression
def test_additem():
    print("adding  items to the cart")
@pytest.mark.skip
@pytest.mark.smoke
@pytest.mark.regression
def test_logout():
    print("logout")
@pytest.mark.skipif(sys.version_info<(3,12),reason="will execute above 3.11 version ")
def test_demo():
    print("Demo skipif ")