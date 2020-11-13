'''
Test requirements according to R7
'''
import pytest
from seleniumbase import BaseCase

from qa327.models import User
from qa327_test.frontend.test_r1 import login_test_user
from qa327_test.conftest import base_url
from unittest.mock import patch
from werkzeug.security import generate_password_hash

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

    @patch('qa327.backend.get_user', return_value= TEST_USER)

    def logout_redirect(self, *_):
        '''see r7.1'''
        #mock backend.get_user to return a test_user instance
        