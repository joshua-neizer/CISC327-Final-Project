'''
Test requirements according to R7
'''
from unittest.mock import patch
from seleniumbase import BaseCase
from werkzeug.security import generate_password_hash
import pytest

from qa327.models import User
from qa327_test.conftest import base_url

#Mock a sample user
TEST_USER = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend'),
    balance=140
)

class R7Test(BaseCase):
    '''
    Contains test cases specific to R7.
    Test only test the frontend portion, and will patch the backend
    specific values
    '''

    def login_test_user(self):
        '''login our test user'''
        self.open(base_url+'/login')
        self.input('#email', TEST_USER.email)
        self.input('#password', 'test_frontend')
        self.click('#btn-submit')

    @patch('qa327.backend.get_user', return_value=TEST_USER)

    def test_logout_redirect(self, *_):
        '''see r7.1'''
        self.open(base_url)
        self.login_test_user()
        self.open(base_url+'/logout')
        assert self.get_current_url() == base_url+'/login'
        message = self.driver.find_element_by_id('login_message')
        assert 'Please Login' in message.text

    def test_logout_restricted(self, *_):
        '''see r7.2'''
        self.login_test_user()
        self.open(base_url+'/logout')
        assert self.get_current_url() == base_url+'/login'
        message = self.driver.find_element_by_id('login_message')
        assert 'Please Login' in message.text
        self.open(base_url)
        assert self.get_current_url() == base_url+'/login'
