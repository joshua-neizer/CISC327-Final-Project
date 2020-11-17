'''
Tests requirements according to R3
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

# Moch some sample tickets
TEST_TICKETS = [
    {'name': 't1', 'price': '100', 'owner': 'god', 'count': 2},
    {'name': 't2', 'price': '90', 'owner': 'geek', 'count': 3},
]


class R3Test(BaseCase):
    '''
    Contains test cases specific to R3
    '''

    def login_test_user(self):
        '''login our test user'''
        self.open(base_url+'/login')
        self.input('#email', TEST_USER.email)
        self.input('#password', 'test_frontend')
        self.click('#btn-submit')

    def assert_flash(self, text):
        '''asserts that message exists in flashes'''
        for flash_dom in self.find_elements('.flash'):
            if flash_dom.text == text:
                return
        raise AssertionError(f'Flash not found for text "{text}"')

    def test_login_redirects(self, *_):
        '''see r3.1'''
        self.open(base_url)
        # verify redirected to /login
        assert self.get_current_url() == base_url+'/login'
        self.assert_element('#login_message')

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_hi_user(self, *_):
        '''see r3.2'''
        self.login_test_user()
        self.open(base_url)
        # use contains check because element also contains
        # balance
        assert 'Hi test_frontend' in self.find_element('#welcome-header').text

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_user_balance(self, *_):
        '''see r3.3'''
        self.login_test_user()
        self.open(base_url)
        # use contains check because element also contains username
        assert (
            'Your balance is $140' in
            self.find_element('#welcome-header').text
        )

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_logout_link(self, *_):
        '''see r3.4'''
        self.login_test_user()
        self.open(base_url)
        self.assert_element('#logout')

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.get_all_tickets', return_value=TEST_TICKETS)
    def test_tickets_listed(self, *_):
        '''see r3.5'''
        self.login_test_user()
        for ticket in TEST_TICKETS:
            name = ticket['name']
            # find div containing ticket info in page
            ticket_div = self.find_element(f'#tickets .ticket[name={name}]')
            # verify all ticket properties match mock
            for prop, value in ticket.items():
                displayed_text = ticket_div.find_element_by_class_name(
                    prop
                ).text
                # assert that displayed ticket property matches
                # mock ticket
                self.assertEqual(displayed_text, str(value))

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_sell_form(self, *_):
        '''see r3.6'''
        self.login_test_user()
        self.open(base_url)
        self.assert_element('#sell-ticket-name')
        self.assert_element('#sell-ticket-quantity')
        self.assert_element('#sell-ticket-price')
        self.assert_element('#sell-ticket-expiration-date')

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_buy_form(self, *_):
        '''see r3.7'''
        self.login_test_user()
        self.open(base_url)
        self.assert_element('#buy-ticket-name')
        self.assert_element('#buy-ticket-quantity')

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_update_form(self, *_):
        '''see r3.8'''
        self.login_test_user()
        self.open(base_url)
        self.assert_element('#update-ticket-name')
        self.assert_element('#update-ticket-quantity')
        self.assert_element('#update-ticket-price')
        self.assert_element('#update-ticket-expiration-date')

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_sell_posts(self, *_):
        '''see r3.9'''
        self.login_test_user()
        self.open(base_url)
        self.input('#sell-ticket-name', 'dont-care')
        self.input('#sell-ticket-quantity', 'dont-care')
        self.input('#sell-ticket-price', 'dont-care')
        self.input('#sell-ticket-expiration-date', 'dont-care')
        self.click('#sell-submit')
        self.assert_flash('ticket sold successfully')

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_buy_posts(self, *_):
        '''see r3.10'''
        self.login_test_user()
        self.open(base_url)
        self.input('#buy-ticket-name', 'dont-care')
        self.input('#buy-ticket-quantity', 'dont-care')
        self.click('#buy-submit')
        self.assert_flash('ticket bought successfully')

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_update_posts(self, *_):
        '''see r3.11'''
        self.login_test_user()
        self.open(base_url)
        self.input('#update-ticket-name', 'dont-care')
        self.input('#update-ticket-quantity', 'dont-care')
        self.input('#update-ticket-price', 'dont-care')
        self.input('#update-ticket-expiration-date', 'dont-care')
        self.click('#update-submit')
        self.assert_flash('ticket updated successfully')