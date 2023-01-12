import pytest
@pytest.mark.parametrize("username,password",[("admin","123Hcl"),("user","123Hcl")])
def test_login(username,password):
    if(username=="admin" and password="123")