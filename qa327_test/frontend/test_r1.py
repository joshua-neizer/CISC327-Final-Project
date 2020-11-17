'''
Test requirements according to R1
'''

from unittest.mock import patch
from seleniumbase import BaseCase
from werkzeug.security import generate_password_hash

from qa327_test.conftest import base_url
from qa327.models import User

# Mock a sample user
TEST_USER = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend'),
    balance=140
)

INVALID_EMAILS = ['test_frontendtest.com', 'test_frontend@.com', 'test\frontend@test.com']

INVALID_PASSWORDS = ['Pass!', 'password123!', 'PASSWORD123!', 'Password123']

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
        assert self.get_current_url() == base_url+'/'

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_form_password_missing(self, *_):
        '''see r1.6'''
        self.open(base_url+'/login')
        self.input('#email', TEST_USER.email)
        self.click('#btn-submit')
        #leave password empty
        message = self.driver.find_element_by_id('password')
        assert message.get_attribute('validationMessage') == 'Please fill out this field.'

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_form_email_missing(self, *_):
        '''see r1.6'''
        self.open(base_url+'/login')
        self.input('#password', 'test_frontend')
        self.click('#btn-submit')
        #leave password empty
        message = self.driver.find_element_by_id('email')
        assert message.get_attribute('validationMessage') == 'Please fill out this field.'

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_email_rfc_specs(self, *_):
        '''see r1.7 (positive)'''
        self.login_test_user()
        assert self.get_current_url() == base_url+'/'

    def test_invalid_email_rfc_specs(self, *_):
        '''see r1.7 (negative)'''
        #invalid email format
        for invalid_email in INVALID_EMAILS:
            self.open(base_url+'/login')
            self.input('#email', invalid_email)
            self.input('#password', 'test_frontend')
            self.click('#btn-submit')
            message = self.driver.find_element_by_class_name('flash')
            assert message.text == 'email/password combination incorrect'
            assert self.get_current_url() == base_url+'/login'

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_password_complexity(self, *_):
        '''see r1.8 (positive)'''
        self.login_test_user()
        assert self.get_current_url() == base_url+'/'

    def test_invalid_password_complexity(self, *_):
        '''see r1.8 (negative)'''
        #invalid password complexity
        for invalid_pass in INVALID_PASSWORDS:
            self.open(base_url+'/login')
            self.input('#email', TEST_USER.email)
            self.input('#password', invalid_pass)
            self.click('#btn-submit')
            message = self.driver.find_element_by_class_name('flash')
            assert message.text == 'email/password combination incorrect'
            assert self.get_current_url() == base_url+'/login'

    def test_invalid_formatting(self, *_):
        '''see r1.9'''
        self.open(base_url+'/login')
        self.input('#email', 'frontendtest.com')
        self.input('#password', 'PASS123')
        self.click('#btn-submit')
        message = self.driver.find_element_by_class_name('flash')
        assert message.text == 'email/password combination incorrect'

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def correct_email_pass(self, *_):
        '''see r1.10'''
        self.login_test_user()
        assert self.get_current_url() == base_url+'/'

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def incorrect_email_pass(self, *_):
        '''see r1.11'''
        self.open(base_url+'/login')
        self.input('#email', TEST_USER.email)
        self.input('#password', 'test123')
        self.click('#btn-submit')
        assert self.get_current_url() == base_url+'/login'
        message = self.driver.find_element_by_class_name('flash')
        assert message.text == 'email/password combination incorrect'
