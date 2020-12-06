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

INVALID_NAMES = ['special^char', 'ticket ', ' ticket']

class R6Test(GeekBaseCase):

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_valid_alpha_name(self, *_):
        '''see r6.1.2, r6.1.4- negative
        ensure ticket name is alphanumeric only, 
        space only allowed in the middle '''
        self.login_test_user()
        self.open(base_url)
        for name in INVALID_NAMES:
            self.input('#buy-ticket-name', name)
            self.input('#buy-ticket-quantity', GOOD_TICKET.quantity)
            self.click('#buy-submit')
            self.assert_flash('Invalid ticket name')
