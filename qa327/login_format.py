import re

def is_password_complex(password):
    return (
        # min length
        len(password)>=6 and
        # has uppercase
        re.search(r'[A-Z]',password) and
        # has lowercase
        re.search(r'[a-z]',password) and
        # has special characters
        re.search(r'[^\w\d\s]',password)
    )

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
NUMBERS = '0123456789'
PRINTABLES = "!#$%&'*+-/=?^_`{|}~"

LOCAL_CHARACTERS = set(
    ALPHABET+ALPHABET.upper()+
    NUMBERS+PRINTABLES+'.'
)

def valid_rfc_local_part(local_part):
    return (
        len(local_part)>0 and
        '..' not in local_part and
        local_part[0]!='.' and
        local_part[-1]!='.' and
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
    return (
        len(domain)>0 and
        domain[0]!='-' and
        domain[-1]!='-' and
        all(
            character in DOMAIN_CHARACTERS
            for character in domain
        )
    )

def valid_rfc_5322(address):
    if address.count('@')!=1:
        return False
    local_part, domain = address.split('@')
    return (
        valid_rfc_local_part(local_part) and
        valid_rfc_domain(domain)
    )

def is_valid_username(username):
    return (
        len(username)>0 and
        username[0]!=' ' and
        username[-1]!=' ' and
        bool(re.match(r'^[\w\d ]+$',username))  
    )