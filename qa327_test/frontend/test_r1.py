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

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_user_login_redirect(self, *_):
        '''see r1.3'''
        self.login_test_user()
        self.open(base_url)
        self.assert_element('#welcome-header')

    def test_login_form(self, *_):
        '''see r1.4'''
        self.open(base_url+'/login')
        self.assert_element('#email')
        self.assert_element('#password')
    
    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_login_submit(self, *_):
        '''see r1.5'''
        self.login_test_user()
        assert self.get_current_url() == base_url

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_form_data_missing(self, *_):
        '''see r1.6'''
        self.open(base_url+'/login')
        # no input for email and password
        self.click('#btn-submit')
        assert 'email/password combination incorrect' in self.find_element('#login_message').text






