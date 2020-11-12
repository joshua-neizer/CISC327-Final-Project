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

    def login_test_user(self):
        '''login our test user'''
        self.open(base_url+'/login')
        self.input('#email', TEST_USER.email)
        self.input('#password', 'test_frontend')
        self.click('#btn-submit')

    def test_login_redirects(self, *_):
        '''see r1.1'''
        self.open(base_url)
        assert self.get_current_url() == base_url+'/login'
        self.assert_element('#login_message')


    def test_login_message(self, *_):
        '''see r1.2'''
        self.open(base_url)
        assert self.get_current_url() == base_url+'/login'
        assert 'Please Login' in self.find_element('#login_message').text