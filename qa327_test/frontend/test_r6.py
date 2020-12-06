'''
Test requirements according to R6
'''

from unittest.mock import patch
from werkzeug.security import generate_password_hash
from qa327_test.conftest import base_url
from qa327_test.frontend.geek_base import GeekBaseCase, TEST_USER, TEST_TICKET
from qa327.models import User

INVALID_NAMES = ['special^char', 'ticket ', ' ticket', 
'loooooooooooooooooooooooooooooooooooooooooooooooooooooooooongname']

INVALID_QUANTITY = ['-1', '101']

BAD_USER = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend'),
    balance=10
)

class R6Test(GeekBaseCase):
    '''
    Contains test cases specific to R6
    '''
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
            self.input('#buy-ticket-quantity', str(TEST_TICKET.quantity))
            self.click('#buy-submit')
            self.assert_flash('Invalid ticket name')
            assert self.get_current_url() == base_url+'/'

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_invalid_quantity(self, *_):
        '''
        see r6.3.2 - negative
        ensure ticket quantity is > 0 and <= 100
        '''
        self.login_test_user()
        self.open(base_url)
        for quantity in INVALID_QUANTITY:
            self.input('#buy-ticket-name', TEST_TICKET.name)
            self.input('#buy-ticket-quantity', quantity)
            self.click('#buy-submit')
            self.assert_flash('Invalid ticket quantity')
            assert self.get_current_url() == base_url+'/'

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.get_ticket', return_value=TEST_TICKET)
    def test_ticket_exists(self, *_):
        '''
        see r6.4.2 - negative
        ensure ticket exists in DB
        '''
        self.login_test_user()
        self.open(base_url)
        self.input('#buy-ticket-name', 'wontexist')
        self.input('#buy-ticket-quantity', str(TEST_TICKET.quantity))
        self.click('#buy-submit')
        self.assert_flash('No such ticket exists')
        assert self.get_current_url() == base_url+'/'

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.get_ticket_byname', return_value=TEST_TICKET)
    def test_ticket_quant(self, *_):
        '''
        see r6.4.4 - negative
        ensure enough tickets in DB
        '''
        self.login_test_user()
        self.open(base_url)
        self.input('#buy-ticket-name', TEST_TICKET.name)
        self.input('#buy-ticket-quantity', str(TEST_TICKET.quantity + 10))
        self.click('#buy-submit')
        self.assert_flash('Not enough tickets available')
        assert self.get_current_url() == base_url+'/'

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.get_ticket_byname', return_value=TEST_TICKET)
    def test_invalid_balance(self, *_):
        '''
        see r6.4.4 - negative
        ensure enough money to buy tickets
        '''
        self.login_test_user()
        self.open(base_url)
        TEST_USER.balance = 1
        self.input('#buy-ticket-name', TEST_TICKET.name)
        self.input('#buy-ticket-quantity', '1')
        self.click('#buy-submit')
        self.assert_flash('Account balance is too low')
        assert self.get_current_url() == base_url+'/'

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.get_ticket_byname', return_value=TEST_TICKET)
    def test_buy_ticket_success(self, *_):
        '''
        see r6.1 - r.6 - positive
        ensures a ticket meeting all the requirements can be bought
        '''
        self.login_test_user()
        self.open(base_url)
        self.input('#buy-ticket-name', TEST_TICKET.name)
        self.input('#buy-ticket-quantity', '1')
        self.click('#buy-submit')
        self.assert_flash('Ticket bought successfully')
