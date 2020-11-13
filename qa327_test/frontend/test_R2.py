  
'''
Tests requirements according to R2
'''

from unittest.mock import patch
from seleniumbase import BaseCase
from werkzeug.security import generate_password_hash

from qa327_test.conftest import base_url
from qa327.models import User

import qa327.backend as bn

# Moch a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password='Password123!',
    password2='Password123!'
)

test_user_bad_nameA= User(
    name=['', 'test_frontend123!', ' test_frontend123', 'test_frontend123 ']
)

test_user_bad_nameB= User(
    name=['te', 'test_frontend1234567890']
)

test_user_bad_email = User(
    email=['', 'test_frontendtest.com', 'test_frontend@testcom', '.test_frontend@test.com']
)

test_user_bad_password = User(
    password=['', 'Pass!', 'password123!', 'PASSWORD123!', 'Password123']
)

test_user_bad_password2A = User(
    password2=['', 'Pass!', 'password123!', 'PASSWORD123!', 'Password123']
)

test_user_bad_password2B = User(
    password2='Password123! '
)

# Moch some sample tickets
TEST_TICKETS = [
    {'name': 't1', 'price': '100', 'owner': 'god', 'count': 2},
    {'name': 't2', 'price': '90', 'owner': 'geek', 'count': 3},
]

class R2Test(BaseCase):
    '''
    Contains test cases specific to R2
    '''

    def positive_case(self, *_):
         # Opens regisration page
        self.open(base_url+'/register')

        # Inputs test user information into the fields
        self.input('#email', test_user.email)
        self.input('#name', test_user.name)
        self.input('#password', test_user.password)
        self.input('#password2', test_user.password2)

        # Submits the inputted information
        self.click('#btn-submit')

        # Asserts that user was registered
        self.assert_text('user registered successfully', '#login_message')

    def r2_1(self, *_):
        '''
        1) Test Case R2.1 - If the user has logged in, redirect back to the 
        user profile page /
        '''
        
        # opens regisration page
        self.open(base_url+'/login')
        # tests if these elements are available
        self.input('#email', test_user.email)
        self.input('#password', 'test_frontend')
        self.click('#btn-submit')
        self.assert_element('#welcome-header')

    def r2_2(self, *_):
        '''
        2) Test Case R2.2 - otherwise, show the user registration page
        '''
        
        # opens regisration page
        self.open(base_url+'/register')
        # tests if these elements are available
        self.assert_element('#register')

    def r2_3(self, *_):
        '''
        3) Test Case R2.3 - the registration page shows a registration form 
        requesting: email, user name, password, password2
        '''
        
        # opens regisration page
        self.open(base_url+'/register')
        # tests if these elements are available
        self.assert_element('#email')
        self.assert_element('#name')
        self.assert_element('#password')
        self.assert_element('#password2')

    def r2_4_pos(self, *_):
        '''
        4) (Positive) Test Case R2.4 - The registration form can be submitted 
        as a [POST] request to the current URL (/register)
        '''

        return self.positive_case()
       

    def r2_4_neg(self, *_):
        '''
        4) (Negative) Test Case R2.4 - The registration form can be submitted 
        as a [POST] request to the current URL (/register)
        '''

        # opens regisration page
        self.open(base_url+'/register')
        self.click('#btn-submit')

        self.assert_text('Email format is incorrect', '#message')




    def r2_5_pos(self, *_):
        '''
        5) (Positive) Test Case R2.5 - Email, password, password2 all have to 
        satisfy the same required as defined in R1
        '''

        return self.positive_case()


    def r2_5_neg_email(self, *_):
        '''
        5) (Negative Email) Test Case R2.5 - Email, password, password2 all have to 
        satisfy the same required as defined in R1

        NOT DONE
        '''

        # opens regisration page
        self.open(base_url+'/register')
        
        for email in test_user_bad_email.email:
            self.input('#name', test_user.name)
            self.input('#password', test_user.password)
            self.input('#password2', test_user.password2)
            self.input("#email", email)
            self.click('#btn-submit')
            self.assert_text('Email format is incorrect', '#message')
            


    def r2_5_neg_password(self, *_):
        '''
        5) (Negative Password) Test Case R2.5 - Email, password, password2 all have to 
        satisfy the same required as defined in R1
        
        Changed frontend.py lines 55 to 58 to check password2
        '''

        # opens regisration page
        self.open(base_url+'/register')

        for password in test_user_bad_password.passord:
            self.input('#email', test_user.email)
            self.input('#name', test_user.name)
            self.input('#password2', test_user.password2)
            self.input("#password", password)
            self.click('#btn-submit')
            self.assert_text('Password format is incorrect', '#message')

    def r2_5_neg_password2(self, *_):
        '''
        5) (Negative Password2) Test Case R2.5 - Email, password, password2 all have to 
        satisfy the same required as defined in R1
        
        NOT DONE
        '''

        self.open(base_url+'/register')

        for password2 in test_user_bad_password2A.password2:
            self.input('#email', test_user.email)
            self.input('#name', test_user.name)
            self.input('#password', test_user.password)
            self.input("#password2", password2)
            self.click('#btn-submit')
            self.assert_text('Password2 format is incorrect', '#message')


    def r2_6_pos(self, *_):
        '''
        6) (Positive) Test Case R2.6 - Password and password2 have to be exactly 
        the same
        '''

        return self.positive_case()


    def r2_6_neg(self, *_):
        '''
        6) (Negative) Test Case R2.6 - Password and password2 have to be exactly 
        the same

        NOT DONE
        '''

        # opens regisration page
        self.open(base_url+'/register')
        self.input('#email', test_user.email)
        self.input('#name', test_user.name)
        self.input('#password', test_user.password)
        self.input('#password2', test_user_bad_password2B.password2)
        self.click('#btn-submit') 
        self.assert_text('The passwords do not match', '#message')


    def r2_7_pos(self, *_):
        '''
        7) (Positive) Test Case R2.7 - User name has to be non-empty, 
        alphanumeric-only, and space allowed only if it is not the first or the 
        last character.
        '''

        return self.positive_case()


    def r2_7_neg(self, *_):
        '''
        7) (Negative) Test Case R2.7 - User name has to be non-empty, 
        alphanumeric-only, and space allowed only if it is not the first or the 
        last character.
        '''

        for name in test_user_bad_nameA.name:
            self.input('#email', test_user.email)
            self.input('#password', test_user.password)
            self.input("#password2", test_user.password2)
            self.input('#name', name)
            self.click('#btn-submit')
            self.assert_text('Username format is incorrect', '#message')


    def r2_8_pos(self, *_):
        '''
        8) (Positive) Test Case R2.8 - User name has to be longer than 2 
        characters and less than 20 characters.
        '''

        return self.positive_case()


    def r2_8_neg(self, *_):
        '''
        8) (Positive) Test Case R2.8 - User name has to be longer than 2 
        characters and less than 20 characters.

        NOT DONE
        '''

        for name in test_user_bad_nameB.name:
            self.input('#email', test_user.email)
            self.input('#password', test_user.password)
            self.input("#password2", test_user.password2)
            self.input('#name', name)
            self.click('#btn-submit')
            self.assert_text('Username format is incorrect', '#message')

    def r2_9(self, *_):
        '''
        9) Test Case R2.9 - For any formatting errors, redirect back to /login 
        and show message '{} format is incorrect.'.format(the_corresponding_attribute)'
        '''

        # Opens regisration page
        self.open(base_url+'/register')

        # Submits the inputted information
        self.click('#btn-submit')


        # Opens regisration page
        self.open(base_url+'/register')


        # Asserts that user was registered
        self.assert_text('user registered successfully', '#login_message')


    def r2_10(self, *_):
        '''
        10) Test Case R2.10 - If the email already exists, show message 
        'this email has been ALREADY used'

        Changed how it checks the email
        '''

        # Opens regisration page
        self.open(base_url+'/register')

        # Inputs test user information into the fields
        self.input('#email', test_user.email)
        self.input('#name', test_user.name)
        self.input('#password', test_user.password)
        self.input('#password2', test_user.password2)

        # Submits the inputted information
        self.click('#btn-submit')

        # Asserts that user was registered
        self.assert_text('User exists', '#message')


    def r2_11(self, *_):
        '''
        11) Test Case R2.11 - If no error regarding the inputs following the 
        rules above, create a new user, set the balance to 5000, and go back to 
        the /login page

        CHANGED HERE
        '''

        self.positive_case()

        self.open(base_url+'/login')
        self.input('#email', test_user.email)
        self.input('#password', test_user.password)

        self.click('#btn-submit')

        self.click('#btn-submit')

        self.open(base_url)
        self.assert_element('#welcome-header')
        assert '$5000' in self.find_element('#welcome-header').text