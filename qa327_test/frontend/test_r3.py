import pytest
from seleniumbase import BaseCase
from unittest.mock import patch
from qa327_test.conftest import base_url
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

# Moch a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend'),
    balance=140
)

# Moch some sample tickets
test_tickets = [
    {'name': 't1', 'price': '100', 'owner':'god','count':2},
    {'name': 't2', 'price': '90','owner':'geek','count':3},
]

class R3Test(BaseCase):

    def login_test_user(self):
        self.open(base_url+'/login')
        self.input('#email',test_user.email)
        self.input('#password','test_frontend')
        self.click('#btn-submit')

    def test_login_redirects(self, *_):
        '''
        see r3.1
        '''
        # open home page
        self.open(base_url)
        # verify redirected to /login
        assert self.get_current_url() == base_url+'/login'
        self.assert_element('#login_message')

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_hi_user(self,*_):
        '''
        see r3.2
        '''
        self.login_test_user()
        # open home page
        self.open(base_url)
        # use contains check because element also contains
        # balance
        assert 'Hi test_frontend' in self.find_element('#welcome-header').text

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_user_balance(self,*_):
        '''
        see r3.3
        '''
        self.login_test_user()
        # open home page
        self.open(base_url)
        # use contains check because element also contains username
        assert 'Your balance is $140' in self.find_element('#welcome-header').text

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_logout_link(self,*_):
        '''
        see r3.4
        '''
        self.login_test_user()
        # open home page
        self.open(base_url)
        self.assert_element('#logout')

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_tickets_listed(self,*_):
        '''
        see r3.5
        '''
        self.login_test_user()
        for ticket in test_tickets:
            name = ticket['name']
            ticket_div = self.find_element(f'#tickets .ticket[name={name}]')
            for prop in ['name','price','owner','count']:
                displayed_text=ticket_div.find_element_by_class_name(prop).text
                # assert that displayed ticket property matches
                # mock ticket
                self.assertEqual(displayed_text,str(ticket[prop]))

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_sell_form(self,*_):
        '''see r3.6'''
        self.login_test_user()
        self.open(base_url)
        self.assert_element('sell-ticket-name')
        self.assert_element('sell-ticket-quantity')
        self.assert_element('sell-ticket-price')
        self.assert_element('sell-ticket-expiration-date')