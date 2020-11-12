'''
Test requirements according to R1
'''

from unittest.mock import patch
from seleniumbase import BaseCase
from werkzeug.security import generate_password_hash

from qa327_test.conftest import base_url
from qa327.models import User

# Moch a sample user
TEST_USER = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend'),
    balance=140
)

class R1Test(BaseCase):
    '''
    Contains test cases specific to R1
    '''