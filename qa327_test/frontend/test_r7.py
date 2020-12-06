'''
Test requirements according to R7
'''
from unittest.mock import patch
from seleniumbase import BaseCase
from werkzeug.security import generate_password_hash
import pytest

from qa327.models import User
from qa327_test.conftest import base_url
from qa327_test.frontend.geek_base import GeekBaseCase, TEST_USER

class R7Test(GeekBaseCase):
    '''
    Contains test cases specific to R7.
    Test only test the frontend portion, and will patch the backend
    specific values
    '''

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
