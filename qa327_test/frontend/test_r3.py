'''
Tests requirements according to R3
'''

from seleniumbase import BaseCase
from unittest.mock import patch
import pytest
from werkzeug.security import generate_password_hash

from qa327_test.conftest import base_url
from qa327.models import User

# Moch a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend'),
    balance=140
)

# Moch some sample tickets
test_tickets = [
    {'name': 't1', 'price': '100', 'owner':'god', 'count':2},
    {'name': 't2', 'price': '90', 'owner':'geek', 'count':3},
]

class R3Test(BaseCase):
    '''
    Contains test cases specific to R3
    '''

    def login_test_user(self):
        self.open(base_url+'/login')
        self.input('#email',test_user.email)
        self.input('#password','test_frontend')
        self.click('#btn-submit')

    def test_login_redirects(self, *_):
        '''see r3.1'''
        self.open(base_url)
        # verify redirected to /login
        assert self.get_current_url() == base_url+'/login'
        self.assert_element('#login_message')

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_hi_user(self,*_):
        '''see r3.2'''
        self.login_test_user()
        self.open(base_url)
        # use contains check because element also contains
        # balance
        assert 'Hi test_frontend' in self.find_element('#welcome-header').text

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_user_balance(self,*_):
        '''see r3.3'''
        self.login_test_user()
        self.open(base_url)
        # use contains check because element also contains username
        assert 'Your balance is $140' in self.find_element('#welcome-header').text

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_logout_link(self,*_):
        '''see r3.4'''
        self.login_test_user()
        self.open(base_url)
        self.assert_element('#logout')

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_tickets_listed(self,*_):
        '''see r3.5'''
        self.login_test_user()
        for ticket in test_tickets:
            name = ticket['name']
            # find div containing ticket info in page
            ticket_div = self.find_element(f'#tickets .ticket[name={name}]')
            # verify all ticket properties match mock
            for key in ticket.keys():
                displayed_text=ticket_div.find_element_by_class_name(key).text
                # assert that displayed ticket property matches
                # mock ticket
                self.assertEqual(displayed_text,str(ticket[key]))

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_sell_form(self,*_):
        '''see r3.6'''
        self.login_test_user()
        self.open(base_url)
        self.assert_element('#sell-ticket-name')
        self.assert_element('#sell-ticket-quantity')
        self.assert_element('#sell-ticket-price')
        self.assert_element('#sell-ticket-expiration-date')

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_buy_form(self,*_):
        '''see r3.7'''
        self.login_test_user()
        self.open(base_url)
        self.assert_element('#buy-ticket-name')
        self.assert_element('#buy-ticket-quantity')

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_update_form(self,*_):
        '''see r3.8'''
        self.login_test_user()
        self.open(base_url)
        self.assert_element('#update-ticket-name')
        self.assert_element('#update-ticket-quantity')
        self.assert_element('#update-ticket-price')
        self.assert_element('#update-ticket-expiration-date')

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_sell_posts(self,*_):
        '''see r3.9'''
        self.login_test_user()
        self.open(base_url)
        self.input('#sell-ticket-name','dont-care')
        self.input('#sell-ticket-quantity','dont-care')
        self.input('#sell-ticket-price','dont-care')
        self.input('#sell-ticket-expiration-date','dont-care')
        self.click('#sell-submit')
        self.assert_text('ticket sold successfully','#post-message')

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_buy_posts(self,*_):
        '''see r3.10'''
        self.login_test_user()
        self.open(base_url)
        self.input('#buy-ticket-name','dont-care')
        self.input('#buy-ticket-quantity','dont-care')
        self.click('#buy-submit')
        self.assert_text('ticket bought successfully','#post-message')

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_update_posts(self,*_):
        '''see r3.11'''
        self.login_test_user()
        self.open(base_url)
        self.input('#update-ticket-name','dont-care')
        self.input('#update-ticket-quantity','dont-care')
        self.input('#update-ticket-price','dont-care')
        self.input('#update-ticket-expiration-date','dont-care')
        self.click('#update-submit')
        self.assert_text('ticket updated successfully','#post-message')