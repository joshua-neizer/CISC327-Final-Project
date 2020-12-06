'''
Test requirements according to R6
'''

from unittest.mock import patch

from qa327_test.conftest import base_url
from qa327_test.frontend.geek_base import GeekBaseCase, TEST_USER
from qa327.models import Ticket
from qa327.ticket_format import parse_date

GOOD_TICKET = Ticket(
    name='helloworld',
    seller_id='1',
    price=20,
    quantity=20,
    expires="20220101"
)

INVALID_NAMES = ['special^char', 'ticket ', ' ticket', 'loooooooooooooooooooooooooooooooooooooooooooooooooooooooooongname']

INVALID_QUANTITY = [-1, 101]

class R6Test(GeekBaseCase):

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_invalid_ticketname(self, *_):
        '''
        see r6.1.2, r6.1.4, r6.2.2- negative
        ensure ticket name is alphanumeric only, 
        space only allowed in the middle
        '''
        self.login_test_user()
        self.open(base_url)
        for name in INVALID_NAMES:
            self.input('#buy-ticket-name', name)
            self.input('#buy-ticket-quantity', (str)GOOD_TICKET.quantity)
            self.click('#buy-submit')
            self.assert_flash('Invalid ticket name')
            self.assert_url('/')

    
    def test_invalid_quantity(self, *_):
        '''
        see r6.3.2 - negative
        ensure ticket quantity is > 0 and <= 100
        '''
        self.login_test_user()
        self.open(base_url)
        for name in INVALID_QUANTITY:
            self.input('#buy-ticket-name', GOOD_TICKET.name)
            self.input('#buy-ticket-quantity', (str)GOOD_TICKET.quantity)
            self.click('#buy-submit')
            self.assert_flash('Invalid ticket quantity')
            self.assert_url('/')

    def test_ticket_exists(self, _*):
        '''
        see r6.4.2 - negative
        ensure ticket exists in DB
        '''
        self.login_test_user()
        self.open(base_url)
        self.input('#buy-ticket-name', 'wontexist')
        self.input('#buy-ticket-quantity', (str)GOOD_TICKET.quantity)
        self.click('#buy-submit')
        self.assert_flash('No such ticket exists')
        self.assert_url('/')

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.sell_ticket(TEST_USER, GOOD_TICKET.quantity, GOOD_TICKET.price, GOOD_TICKET.price, GOOD_TICKET.expires)', return_value = 'ticket sold successfully')
    def test_ticket_quant(self, _*):
        '''
        see r6.4.4 - negative
        ensure enough tickets in DB
        '''
        self.login_test_user()
        self.open(base_url)
        self.input('#buy-ticket-name', GOOD_TICKET.name)
        self.input('#buy-ticket-quantity', '50')
        self.click('#buy-submit')
        self.assert_flash('Not enough tickets available')
        self.assert_url('/')

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_invalid_balance(self, *_):
        '''
        see r6.4.4 - negative
        ensure enough money to buy tickets
        TODO: FINISH THIS
        how to mock user's balance to be different?
        '''
        TEST_USER.balance = 10
        self.login_test_user()
        self.open(base_url)
        self.input('#buy-ticket-name', GOOD_TICKET.name)
        self.input('#buy-ticket-quantity', (str)GOOD_TICKET.quantity)
        self.click('#buy-submit')
        self.assert_flash('Account balance is too low')
        self.assert_url('/')

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.sell_ticket(TEST_USER, GOOD_TICKET.quantity, GOOD_TICKET.price, GOOD_TICKET.price, GOOD_TICKET.expires)', return_value = 'ticket sold successfully')
    def test_buy_ticket_success(self, *_):
        '''
        see r6.1 - r.6 - positive
        ensures a ticket meeting all the requirements can be bought
        '''
        self.login_test_user()
        self.open(base_url)
        self.input('#buy-ticket-name', GOOD_TICKET.name)
        self.input('#buy-ticket-quantity', (str)GOOD_TICKET.quantity)
        self.click('#buy-submit')
        self.assert_flash('Ticket bought successfully')
