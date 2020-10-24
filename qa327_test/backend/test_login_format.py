import pytest
from qa327.login_format import (
    is_valid_password,is_valid_username,
    is_valid_email
)

def test_is_valid_password():
    assert is_valid_password('Password!')
    assert not is_valid_password('password!')
    assert not is_valid_password('PASSWORD!')
    assert not is_valid_password('Password')

def test_rfc_5322():
    assert is_valid_email('john.smith@gmail.com')
    assert not is_valid_email('john.smith.@gmail.com')
    assert not is_valid_email('john..smith.@gmail.com')
    assert is_valid_email('john.smith@g-mail.com')
    assert not is_valid_email('john.smith@-gmail.com')
    assert not is_valid_email('john.smith@gmail-.com')
    assert not is_valid_email('nonsense')

def test_is_valid_username():
    assert is_valid_username('johnsmith123')
    assert is_valid_username('space in between')
    assert not is_valid_username(' space around edge ')
    assert not is_valid_username('special character $$$')