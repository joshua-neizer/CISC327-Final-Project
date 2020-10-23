import pytest
from qa327.password import is_password_complex

def test_is_password_complex():
    assert is_password_complex('Password!')
    assert not is_password_complex('password!')
    assert not is_password_complex('PASSWORD!')
    assert not is_password_complex('Password')