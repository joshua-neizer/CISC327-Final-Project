import pytest
from qa327.login_format import (
    is_password_complex,is_valid_username,
    valid_rfc_5322
)

def test_is_password_complex():
    assert is_password_complex('Password!')
    assert not is_password_complex('password!')
    assert not is_password_complex('PASSWORD!')
    assert not is_password_complex('Password')

def test_rfc_5322():
    assert valid_rfc_5322('john.smith@gmail.com')
    assert not valid_rfc_5322('john.smith.@gmail.com')
    assert not valid_rfc_5322('john..smith.@gmail.com')
    assert valid_rfc_5322('john.smith@g-mail.com')
    assert not valid_rfc_5322('john.smith@-gmail.com')
    assert not valid_rfc_5322('john.smith@gmail-.com')
    assert not valid_rfc_5322('nonsense')

def test_is_valid_username():
    assert is_valid_username('johnsmith123')
    assert is_valid_username('space in between')
    assert not is_valid_username(' space around edge ')
    assert not is_valid_username('special character $$$')