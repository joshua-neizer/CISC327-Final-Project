"""helper functions for login format verification"""
import re

def is_valid_password(password):
    """Validate password with provided requirements

    inputs:
    password -- a string password
    outputs:
    true if the password is acceptable, false otherwise
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
    ALPHABET+ALPHABET.upper()+
    NUMBERS+PRINTABLES+'.'
)

def valid_rfc_local_part(local_part):
    """Validate local part of email with RFC 5322 requirements

    inputs:
    local_part -- local part as string
    output:
    true if the email is acceptable, false otherwise
    """
    return (
        len(local_part) > 0 and
        '..' not in local_part and
        local_part[0] != '.' and
        local_part[-1] != '.' and
        all(
            character in LOCAL_CHARACTERS
            for character in local_part
        )
    )

DOMAIN_CHARACTERS = set(
    ALPHABET+ALPHABET.upper()+
    NUMBERS+'-.'
)

def valid_rfc_domain(domain):
    """Validate domain part of email with RFC 5322 requirements

    inputs:
    domain -- domain as string
    output:
    true if the email is acceptable, false otherwise
    """
    return (
        len(domain) > 0 and
        domain[0] != '-' and
        domain[-1] != '-' and
        all(
            character in DOMAIN_CHARACTERS
            for character in domain
        )
    )

# obeys rfc 5322
def is_valid_email(address):
    """Validate email with RFC 5322 requirements and calls 2 helpers functions

    inputs:
    address -- email address as string
    output:
    true if the email is acceptable, false otherwise
    """
    if address.count('@') != 1:
        return False
    local_part, domain = address.split('@')
    return (
        valid_rfc_local_part(local_part) and
        valid_rfc_domain(domain)
    )

def is_valid_username(username):
    """Validate username with provided requirements

    inputs:
    username -- a string
    output:
    true if the username is acceptable, false otherwise
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
