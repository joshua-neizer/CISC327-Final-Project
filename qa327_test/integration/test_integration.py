'''
stores integration tests that verify both frontend
and backend function in harmony
'''

import re
from collections import namedtuple
from qa327_test.frontend.geek_base import GeekBaseCase
from qa327_test.conftest import base_url

WhiteBoxUser = namedtuple('WhiteBoxUser',[
    'email', 'name', 'password'
])

TEST_USER_ALONE = WhiteBoxUser(
    email='testuser1@gmail.com',
    name='testuser1',
    password='Password99!'
)
TEST_USER_SELLER = WhiteBoxUser(
    email='seller@gmail.com',
    name='seller',
    password='Password99!'
)
TEST_USER_BUYER = WhiteBoxUser(
    email='buyer@gmail.com',
    name='buyer',
    password='Password99!'
)

WhiteBoxTicket = namedtuple('WhiteBoxTicket', [
    'name', 'quantity', 'price', 'expires'
])

TEST_TICKET = WhiteBoxTicket(
    name='testticket',
    quantity='21',
    price='35',
    expires='20220101'
)
TEST_TICKET_AFTER_UPDATE = WhiteBoxTicket(
    name='testticket',
    quantity='21',
    price='36',
    expires='20220101'
)

TICKET_BEFORE_BUY = WhiteBoxTicket(
    name='purchasetestticket',
    quantity='21',
    price='20',
    expires='20220101'
)

TICKET_AFTER_BUY = WhiteBoxTicket(
    name='purchasetestticket',
    quantity='20',
    price='20',
    expires='20220101'
)

def digits_only(text):
    return re.sub(r'\D', '', text)

class IntegrationTest(GeekBaseCase):
    def register_user(self, user):
        self.click('#register-button')
        self.input('#email', user.email)
        self.input('#name', user.name)
        self.input('#password', user.password)
        self.input('#password2', user.password)
        self.click('#register-submit')

    def login_user(self, user):
        self.input('#email', user.email)
        self.input('#password', user.password)
        self.click('#btn-submit')

    def sell_ticket(self, ticket):
        self.input('#sell-ticket-name', ticket.name)
        self.input('#sell-ticket-quantity', ticket.quantity)
        self.input('#sell-ticket-price', ticket.price)
        self.input('#sell-ticket-expiration-date', ticket.expires)
        self.click('#sell-submit')

    def assert_ticket_listed(self, ticket):
        ticket_element = self.find_element(
            f'#tickets .ticket[name="{ticket.name}"]'
        )
        def displayed_value(prop):
            element = ticket_element.find_element_by_class_name(prop)
            return element.text
        
        self.assertEqual(
            displayed_value('name'),
            ticket.name
        )
        self.assertEqual(
            displayed_value('quantity'),
            ticket.quantity
        )
        self.assertEqual(
            digits_only(displayed_value('expires')),
            ticket.expires
        )

    def update_ticket(self, name, price):
        self.input('#sell-ticket-name', name)
        self.input('#sell-ticket-quantity', str(price))
        self.click('#update-submit')

    def test_create_posting(self):
        self.open(base_url)
        self.register_user(TEST_USER_ALONE)
        self.login_user(TEST_USER_ALONE)
        self.sell_ticket(TEST_TICKET)
        self.assert_ticket_listed(TEST_TICKET)
        self.update_ticket(TEST_TICKET.name, price=36)
        self.assert_ticket_listed(TEST_TICKET_AFTER_UPDATE)
        self.click('#logout')

    def read_balance(self):
        return int(self.find_element('#user-balance').text)

    def buy_ticket(self, name, quantity):
        self.input('#buy-ticket-name', name)
        self.input('#buy-ticket-quantity', str(quantity))
        self.click('#buy-submit')

    def list_ticket(self):
        self.open(base_url)
        self.register_user(TEST_USER_SELLER)
        self.login_user(TEST_USER_SELLER)
        self.sell_ticket(TICKET_BEFORE_BUY)
        self.click('#logout')

    def test_purchase_ticket(self):
        self.list_ticket()
        self.register_user(TEST_USER_BUYER)
        self.login_user(TEST_USER_BUYER)
        initial_balance = self.read_balance()
        self.buy_ticket(
            TICKET_BEFORE_BUY.name,
            1
        )
        # assert that ticket quantity decreased
        self.assert_ticket_listed(TICKET_AFTER_BUY)

        total_cost = int(int(TICKET_AFTER_BUY.price)*1.4)
        # assert that buyer balance decreased
        self.assertEqual(
            self.read_balance(),
            initial_balance-total_cost
        )
        # check that seller balance increased
        self.click('#logout')
        self.login_user(TEST_USER_SELLER)
        self.assertEqual(
            self.read_balance(),
            initial_balance+int(TICKET_AFTER_BUY.price)
        )