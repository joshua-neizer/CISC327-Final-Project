from collections import namedtuple
from qa327_test.frontend.geek_base import GeekBaseCase
from qa327_test.conftest import base_url

WhiteBoxUser = namedtuple('WhiteBoxUser',[
    'email','name','password'
])

TEST_USER_1 = WhiteBoxUser(
    email='testuser1@gmail.com',
    name='testuser1',
    password='Password99!'
)
TEST_USER_2 = WhiteBoxUser(
    email='testuser2@gmail.com',
    name='testuser2',
    password='Password99!'
)

WhiteBoxTicket = namedtuple('WhiteBoxTicket',[
    'name','quantity','price','expires'
])

TEST_TICKET = WhiteBoxTicket(
    name='testticket',
    quantity='21',
    price='35',
    expires='20220101'
)
TEST_TICKET_V2 = WhiteBoxTicket(
    name='testticket',
    quantity='21',
    price='36',
    expires='20220101'
)

class IntegrationTest(GeekBaseCase):
    def register_user(self, user):
        self.open(base_url)
        self.click('#register-button')
        self.input('#email',user.email)
        self.input('#name',user.name)
        self.input('#password',user.password)
        self.input('#password2',user.password)
        self.click('#btn-submit')

    def login_user(self, user):
        self.input('#email',user.email)
        self.input('#password',user.password)
        self.click('#btn-submit')

    def sell_ticket(self, user, ticket):
        self.input('#sell-ticket-name',ticket.name)
        self.input('#sell-ticket-quantity',ticket.quantity)
        self.input('#sell-ticket-price', ticket.price)
        self.input('#ticket-expiration-date', ticket.expires)
        self.click('#sell-submit')

    def assert_ticket_listed(self, ticket):
        tickets = self.find_elements('#tickets .ticket')
        self.assertEqual(len(tickets),1)
        ticket = tickets[0]
        def displayed_value(prop):
            element = ticket.find_element_by_class_name(prop)
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
            displayed_value('expires'),
            ticket.expires
        )

    def update_ticket(self, name, price):
        self.input('#sell-ticket-name',name)
        self.input('#sell-ticket-quantity',price)
        self.click('#update-submit')

    def test_create_posting(self):
        self.register_user(TEST_USER_1)
        self.login_user(TEST_USER_1)
        self.sell_ticket(TEST_USER_1,TEST_TICKET)
        self.assert_ticket_listed(TEST_TICKET)
        self.update_ticket(TEST_TICKET.name,price=36)
        self.assert_ticket_listed(TEST_TICKET_V2)