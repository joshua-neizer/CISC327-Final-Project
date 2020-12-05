'''
Test requirements according to R4
'''

from unittest.mock import patch

from qa327_test.conftest import base_url
from qa327_test.frontend.geek_base import GeekBaseCase, TEST_USER
from qa327.models import Ticket
from qa327.ticket_format import parse_date

# Test Information
GOOD_TICKET = Ticket(
    name='helloworld',
    seller_id='1',
    price=20,
    quantity=20,
    expires="20220101"
)

GOOD_TICKET_DICT = [{'name': 'helloworld', 'price': '20', 'owner': 'jesus', 'count': '20'}]

INVALID_NAME_FORMATS = ['bad', ' alsobad', 'alsobad ', '$alsobad$',
                        'veeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeerylongname']

INVALID_QUANTITIES = [-1, 101]

INVALID_PRICES = [5, 101]

INVALID_DATES = ['January 1 2024', '20200204']

class R4Test(GeekBaseCase):
    '''
    Contains test cases specific to R4
    '''

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_ticket_name(self, *_):
        '''
        See r4.1/r4.2 - Negative
        Checks all invalid formats with spaces, special characters,
        and name length
        '''
        self.login_test_user()
        self.open(base_url)
        for name in INVALID_NAME_FORMATS:
            self.input('#sell-ticket-name', name)
            self.input('#sell-ticket-quantity', GOOD_TICKET.quantity)
            self.input('#sell-ticket-price', GOOD_TICKET.price)
            self.input('#sell-ticket-expiration-date', '20220101')
            self.click('#sell-submit')
            self.assert_flash('Invalid ticket name')

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_ticket_quantity(self, *_):
        '''
        See r4.3 - Negative
        Checks all invalid ticket quantities
        '''
        self.login_test_user()
        self.open(base_url)
        for quantity in INVALID_QUANTITIES:
            self.input('#sell-ticket-name', GOOD_TICKET.name)
            self.input('#sell-ticket-quantity', quantity)
            self.input('#sell-ticket-price', GOOD_TICKET.price)
            self.input('#sell-ticket-expiration-date', '20220101')
            self.click('#sell-submit')
            self.assert_flash('Invalid ticket quantity')

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_ticket_price(self, *_):
        '''
        See r4.4 - Negative
        Checks all invalid ticket prices
        '''
        self.login_test_user()
        self.open(base_url)
        for price in INVALID_PRICES:
            self.input('#sell-ticket-name', GOOD_TICKET.name)
            self.input('#sell-ticket-quantity', GOOD_TICKET.quantity)
            self.input('#sell-ticket-price', price)
            self.input('#sell-ticket-expiration-date', '20220101')
            self.click('#sell-submit')
            self.assert_flash('Invalid ticket price')

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_ticket_date(self, *_):
        '''
        See r4.5 - Negative
        Checks all invalid ticket expiration dates
        '''
        self.login_test_user()
        self.open(base_url)
        for date in INVALID_DATES:
            self.input('#sell-ticket-name', GOOD_TICKET.name)
            self.input('#sell-ticket-quantity', GOOD_TICKET.quantity)
            self.input('#sell-ticket-price', GOOD_TICKET.price)
            self.input('#sell-ticket-expiration-date', date)
            self.click('#sell-submit')
            self.assert_flash('Invalid ticket date')

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.sell_ticket', return_value='ticket sold successfully')
    @patch('qa327.backend.get_all_tickets')
    def test_good_ticket(self, get_all_tickets_function, *_):
        '''
        See r4.6
        Ticket with proper format will be posted to profile page
        '''
        self.login_test_user()
        self.open(base_url)

        get_all_tickets_function.return_value = []

        self.input('#sell-ticket-name', GOOD_TICKET.name)
        self.input('#sell-ticket-quantity', GOOD_TICKET.quantity)
        self.input('#sell-ticket-price', GOOD_TICKET.price)
        self.input('#sell-ticket-expiration-date', GOOD_TICKET.expires)
        self.click('#sell-submit')
        self.assert_flash('ticket sold successfully')

        get_all_tickets_function.return_value = GOOD_TICKET_DICT
        self.refresh()
        name = GOOD_TICKET.name

        ticket_div = self.find_element(f'#tickets .ticket[name={name}]')
        for prop, value in GOOD_TICKET_DICT[0].items():
            displayed_text = ticket_div.find_element_by_class_name(prop).text
            self.assertEqual(displayed_text, str(value))
