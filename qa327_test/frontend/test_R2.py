'''
Tests requirements according to R2
'''

from unittest.mock import patch
from werkzeug.security import generate_password_hash
from seleniumbase import BaseCase
from qa327_test.conftest import base_url

import qa327.models

# Defines user class to make testing more streamlined
class User:
    def __init__(self, email=None, name=None, password=None):
        self.email = email
        self.name = name
        self.password = password


# Defines test information
TEST_USER_A = qa327.models.User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password123!', method='sha256'),
    balance=5000
)

TEST_USER_B = qa327.models.User(
    email='test_frontend@test.com',
    name='test_frontend',
    password='Password123!'
)


VALID_USER = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password='Password123!'
)

INVALID_USER_NAME_A = User(
    name=['', 'test_frontend123!', ' test_frontend123', 'test_frontend123 ']
)

INVALID_USER_NAME_B = User(
    name=['te', 'test_frontend1234567890']
)

INVALID_USER_EMAIL = User(
    email=['', 'test_frontendtest.com', 'test_frontend@testcom', '.test_frontend@test.com']
)

INVALID_USER_PASSWORD = User(
    password=['', 'Pass!', 'password123!', 'PASSWORD123!', 'Password123']
)

MISMATCHED_PASSWORD2 = User(
    password='Password123! '
)

class R2Test(BaseCase):
    '''
    Contains test cases specific to R2
    '''

    def register_test_user(self, *_):
        '''register our test user'''

         # Opens regisration page
        self.open(base_url+'/register')

        # Inputs test user information into the fields
        self.input('#email', VALID_USER.email)
        self.input('#name', VALID_USER.name)
        self.input('#password', VALID_USER.password)
        self.input('#password2', VALID_USER.password)

        # Submits the inputted information
        self.click('#register-submit')


    def login_test_user(self):
        '''login our test user'''
        # Opens login page
        self.open(base_url+'/login')

        # Logins in with user information
        self.input('#email', TEST_USER_A.email)
        self.input('#password', VALID_USER.password)

        # Submits the inputted information
        self.click('#btn-submit')


    # @patch('qa327.backend.get_user', return_value=TEST_USER_A)
    # def test_r2_1(self, *_):
    #     '''
    #     1) Test Case R2.1 - If the user has logged in, redirect back to the
    #     user profile page /
    #     '''

    #     # Logs in user to
    #     self.login_test_user()

    #     # Opens the user profile page /
    #     self.open(base_url)

    #     # Verifies that the page contains the welcome header
    #     self.assert_element('#welcome-header')

    # def test_r2_2(self, *_):
    #     '''
    #     2) Test Case R2.2 - otherwise, show the user registration page
    #     '''

    #     # opens regisration page
    #     self.open(base_url+'/register')
    #     # tests if these elements are available
    #     self.assert_element('#register')


    # def test_r2_3(self, *_):
    #     '''
    #     3) Test Case R2.3 - the registration page shows a registration form
    #     requesting: email, user name, password, password2
    #     '''

    #     # Opens regisration page
    #     self.open(base_url+'/register')

    #     # Tests if these elements are on the page
    #     self.assert_element('#email')
    #     self.assert_element('#name')
    #     self.assert_element('#password')
    #     self.assert_element('#password2')


    # @patch('qa327.backend.get_user', return_value=[])
    # @patch('qa327.backend.register_user', return_value=True)
    # def test_r2_4(self, *_):
    #     '''
    #     4) Test Case R2.4 - The registration form can be submitted
    #     as a [POST] request to the current URL (/register)
    #     '''
    #     # Registers user
    #     self.register_test_user()

    #     # Verifies that the user has successfully registered
    #     self.assert_text('User registered successfully', '#login_message')

    #     # Verifies that the user is redirected to login page
    #     assert self.get_current_url() == base_url+'/login'


    # @patch('qa327.backend.get_user', return_value=[])
    # @patch('qa327.backend.register_user', return_value=True)
    # def test_r2_5_pos(self, *_):
    #     '''
    #     5) (Positive) Test Case R2.5 - Email, password, password2 all have to
    #     satisfy the same required as defined in R1
    #     '''

    #     # Registers user
    #     self.register_test_user()

    #     # Asserts that user successfully registered
    #     self.assert_text('User registered successfully', '#login_message')



    # def test_r2_5_neg_email(self, *_):
    #     '''
    #     5) (Negative Email) Test Case R2.5 - Email, password, password2 all have to
    #     satisfy the same required as defined in R1
    #     '''

    #     # Opens registration page and iterates over invalid email addresses, along
    #     # with remaining valid information to verifies that there is an error message
    #     # and there is no POST
    #     for email in INVALID_USER_EMAIL.email:
    #         self.open(base_url+'/register')
    #         self.input('#name', VALID_USER.name)
    #         self.input('#password', VALID_USER.password)
    #         self.input('#password2', VALID_USER.password)
    #         self.input("#email", email)
    #         self.click('#register-submit')
    #         assert 'Email format is incorrect' in self.find_element('#login_message').text


    # def test_r2_5_neg_password(self, *_):
    #     '''
    #     5) (Negative Password) Test Case R2.5 - Email, password, password2 all have to
    #     satisfy the same required as defined in R1

    #     Changed frontend.py lines 55 to 58 to check password2
    #     '''

    #      # Opens registration page and iterates over invalid passwords, along
    #     # with remaining valid information to verifies that there is an error message
    #     # and there is no POST

    #     for password in INVALID_USER_PASSWORD.password:
    #         self.open(base_url+'/register')
    #         self.input('#email', VALID_USER.email)
    #         self.input('#name', VALID_USER.name)
    #         self.input('#password2', VALID_USER.password)
    #         self.input("#password", password)
    #         self.click('#register-submit')
    #         assert 'Password format is incorrect' in self.find_element('#login_message').text

    # def test_r2_5_neg_password2(self, *_):
    #     '''
    #     5) (Negative Password2) Test Case R2.5 - Email, password, password2 all have to
    #     satisfy the same required as defined in R1
    #     '''

    #     # Opens registration page and iterates over invalid password2s, along
    #     # with remaining valid information to verifies that there is an error message
    #     # and there is no POST
    #     for password2 in INVALID_USER_PASSWORD.password:
    #         self.open(base_url+'/register')
    #         self.input('#email', VALID_USER.email)
    #         self.input('#name', VALID_USER.name)
    #         self.input('#password', VALID_USER.password)
    #         self.input("#password2", password2)
    #         self.click('#register-submit')
    #         assert 'Password2 format is incorrect' in self.find_element('#login_message').text


    # @patch('qa327.backend.get_user', return_value=[])
    # @patch('qa327.backend.register_user', return_value=True)
    # def test_r2_6_pos(self, *_):
    #     '''
    #     6) (Positive) Test Case R2.6 - Password and password2 have to be exactly
    #     the same
    #     '''

    #     # Registers user
    #     self.register_test_user()

    #     # Asserts that user successfully registered
    #     self.assert_text('User registered successfully', '#login_message')


    # def test_r2_6_neg(self, *_):
    #     '''
    #     6) (Negative) Test Case R2.6 - Password and password2 have to be exactly
    #     the same
    #     '''

    #     # Opens regisration page
    #     self.open(base_url+'/register')

    #     # Inputs valid user information
    #     self.input('#email', VALID_USER.email)
    #     self.input('#name', VALID_USER.name)
    #     self.input('#password', VALID_USER.password)

    #     # Enters different string for password2 than for password
    #     self.input('#password2', MISMATCHED_PASSWORD2.password)

    #     # Submits information
    #     self.click('#register-submit')


    #     # Verifies that there is an error message and there is no POST
    #     assert 'The passwords do not match' in self.find_element('#login_message').text


    # @patch('qa327.backend.get_user', return_value=[])
    # @patch('qa327.backend.register_user', return_value=True)
    # def test_r2_7_pos(self, *_):
    #     '''
    #     7) (Positive) Test Case R2.7 - User name has to be non-empty,
    #     alphanumeric-only, and space allowed only if it is not the first or the
    #     last character.
    #     '''

    #     # Registers user
    #     self.register_test_user()

    #     # Asserts that user successfully registered
    #     self.assert_text('User registered successfully', '#login_message')


    # def test_r2_7_neg(self, *_):
    #     '''
    #     7) (Negative) Test Case R2.7 - User name has to be non-empty,
    #     alphanumeric-only, and space allowed only if it is not the first or the
    #     last character.
    #     '''

    #     # Opens registration page and iterates over invalid user names, along
    #     # with remaining valid information to verifies that there is an error message
    #     # and there is no POST
    #     for name in INVALID_USER_NAME_A.name:
    #         self.open(base_url+'/register')
    #         self.input('#email', VALID_USER.email)
    #         self.input('#password', VALID_USER.password)
    #         self.input('#password2', VALID_USER.password)
    #         self.input('#name', name)
    #         self.click('#register-submit')
    #         assert 'Username format is incorrect' in self.find_element('#login_message').text


    # @patch('qa327.backend.get_user', return_value=[])
    # @patch('qa327.backend.register_user', return_value=True)
    # def test_r2_8_pos(self, *_):
    #     '''
    #     8) (Positive) Test Case R2.8 - User name has to be longer than 2
    #     characters and less than 20 characters.
    #     '''

    #     # Registers user
    #     self.register_test_user()

    #     # Asserts that user successfully registered
    #     self.assert_text('User registered successfully', '#login_message')


    # def test_r2_8_neg(self, *_):
    #     '''
    #     8) (Positive) Test Case R2.8 - User name has to be longer than 2
    #     characters and less than 20 characters.
    #     '''

    #     # Opens registration page and iterates over invalid user names, along
    #     # with remaining valid information to verifies that there is an error message
    #     # and there is no POST
    #     for name in INVALID_USER_NAME_B.name:
    #         self.open(base_url+'/register')
    #         self.input('#email', VALID_USER.email)
    #         self.input('#password', VALID_USER.password)
    #         self.input("#password2", VALID_USER.password)
    #         self.input('#name', name)
    #         self.click('#register-submit')
    #         assert 'Username format is incorrect' in self.find_element('#login_message').text

    # def test_r2_9(self, *_):
    #     '''
    #     9) Test Case R2.9 - For any formatting errors, redirect back to /login
    #     and show message '{} format is incorrect.'.format(the_corresponding_attribute)'
    #     '''

    #     # Opens regisration page
    #     self.open(base_url+'/register')

    #     # Submits the inputted information
    #     self.click('#register-submit')

    #     # Asserts that user was registered
    #     self.assert_text('Email format is incorrect', '#login_message')

    #     # Verifies that the user is redirected to login page
    #     assert self.get_current_url() == base_url+'/login'


    # @patch('qa327.backend.get_user', return_value=TEST_USER_B)
    # def test_r2_10(self, *_):
    #     '''
    #     10) Test Case R2.10 - If the email already exists, show message
    #     'this email has been ALREADY used'

    #     Changed how it checks the email
    #     '''

    #     # Opens regisration page
    #     self.open(base_url+'/register')

    #     # Inputs test user information into the fields
    #     self.input('#email', VALID_USER.email)
    #     self.input('#name', VALID_USER.name)
    #     self.input('#password', VALID_USER.password)
    #     self.input('#password2', VALID_USER.password)

    #     # Submits the inputted information
    #     self.click('#register-submit')

    #     # Asserts that user was registered
    #     self.assert_text('User exists', '#message')

    @patch('qa327.backend.register_user', return_value=True)
    @patch('qa327.backend.get_user', side_effect=[[], TEST_USER_A, TEST_USER_A, TEST_USER_A])
    def test_r2_11(self, *_):
        '''
        11) Test Case R2.11 - If no error regarding the inputs following the
        rules above, create a new user, set the balance to 5000, and go back to
        the /login page

        CHANGED HERE
        '''

        # Registers user
        self.register_test_user()

        # Asserts that user successfully registered
        self.assert_text('User registered successfully', '#login_message')

        # Logs in user with newly registered user
        self.login_test_user()

        # Opens the user profile page /
        self.open(base_url)

        # Asserts there is a welcome-header id
        self.assert_element('#welcome-header')

        # Asserts new user has a balance of $5000
        assert '$5000' in self.find_element('#welcome-header').text