"""helper functions for login format verification"""
import re
import validate_email


def is_valid_password(password):
    """
    Validate password with provided requirements
    :param password: a string password
    :return true if the password is acceptable, false otherwise
    """
    return (
        # min length
        len(password) >= 6 and
        # has uppercase
        re.search(r'[A-Z]', password) and
        # has lowercase
        re.search(r'[a-z]', password) and
        # has special characters
        re.search(r'[^\w\d\s]', password)
    )


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
NUMBERS = '0123456789'
PRINTABLES = "!#$%&'*+-/=?^_`{|}~"

LOCAL_CHARACTERS = set(
    ALPHABET + ALPHABET.upper() +
    NUMBERS + PRINTABLES+'.'
)


# obeys rfc 5322
def is_valid_email(address):
    """
    Validate email with RFC 5322 requirements using the validate_email library
    :param address: email address as string
    :return true if the email is acceptable, false otherwise
    """
    return validate_email.validate_email(email_address=address,
                                         check_regex=True, check_mx=False)


def is_valid_username(username):
    """
    Validate username with provided requirements
    :param username: username of user trying to login
    :return true if the username is acceptable, false otherwise
    """
    return (
        # r2.8 requirement
        2 < len(username) < 20 and
        # does not start or end with space
        username[0] != ' ' and
        username[-1] != ' ' and
        # is alphanumeric (plus space)
        bool(re.match(r'^[\w\d ]+$', username))
    )
