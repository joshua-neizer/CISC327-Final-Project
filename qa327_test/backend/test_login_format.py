import pytest
from qa327.login_format import is_password_complex,valid_rfc_5322

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