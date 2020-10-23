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