'''
Tests requirements according to R3
'''

from unittest.mock import patch
from dateutil.parser import parse as parse_date

from qa327_test.conftest import base_url
from qa327_test.frontend.geek_base import GeekBaseCase, TEST_USER
from qa327.models import Ticket


# Moch some sample tickets
TEST_TICKETS = [
    {'name': 't1', 'price': '100', 'owner': 'god', 'count': 2},
    {'name': 't2', 'price': '90', 'owner': 'geek', 'count': 3},
]

HELLO_TICKET = Ticket(
    name='helloworld',
    seller_id='1',
    price=20,
    quantity=20,
    expires=parse_date("January 1 2022")
)

class R3Test(GeekBaseCase):
    '''
    Contains test cases specific to R3
    '''

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
        self.assert_element('#update-upt-ticket-name')
        self.assert_element('#update-ticket-quantity')
        self.assert_element('#update-ticket-price')
        self.assert_element('#update-ticket-expiration-date')

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.sell_ticket', return_value='ticket sold successfully')
    def test_sell_posts(self, *_):
        '''see r3.9'''
        self.login_test_user()
        self.open(base_url)
        self.input('#sell-ticket-name', 'helloworld')
        self.input('#sell-ticket-quantity', '20')
        self.input('#sell-ticket-price', '20')
        self.input('#sell-ticket-expiration-date', '20220101')
        self.click('#sell-submit')
        self.assert_flash('ticket sold successfully')

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.get_ticket',return_value=HELLO_TICKET)
    @patch('qa327.backend.buy_ticket', return_value='Ticket bought successfully')
    def test_buy_posts(self, *_):
        '''see r3.10'''
        self.login_test_user()
        self.open(base_url)
        self.input('#buy-ticket-name', 'helloworld')
        self.input('#buy-ticket-quantity', '5')
        self.click('#buy-submit')
        self.assert_flash('Ticket bought successfully')

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.update_ticket', return_value='ticket updated successfully')
    def test_update_posts(self, *_):
        '''see r3.11'''
        self.login_test_user()
        self.open(base_url)
        self.input('#update-prev-ticket-name', 'helloworld')
        self.input('#update-upt-ticket-name', 'helloworld')
        self.input('#update-ticket-quantity', '20')
        self.input('#update-ticket-price', '20')
        self.input('#update-ticket-expiration-date', '20220101')
        self.click('#update-submit')
        self.assert_flash('User updated ticket successfully')
