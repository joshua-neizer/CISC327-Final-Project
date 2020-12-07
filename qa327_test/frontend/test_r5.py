'''
Tests requirements according to R2
'''

from unittest.mock import patch
from werkzeug.security import generate_password_hash

from qa327.models import User, Ticket
from qa327_test.conftest import base_url
from qa327_test.frontend.geek_base import GeekBaseCase

# Defines test information
TEST_USER = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('Password123!', method='sha256'),
    balance=5000
)

TEST_TICKET = Ticket(
    name='test_ticket',
    price='20',
    quantity='20',
    expires='20211208'
)

UPDATED_TEST_TICKET = Ticket(
    name='updated_test _ticket',
    price='40',
    quantity='100',
    expires='20221208'
)


INVALID_TICKET_NAME_FORMATS = [
    '$$$special$characters$$$',
    ' spacebefore', 'spaceafter '
]

INVALID_TICKET_NAME_LENGTHS = [
    've', 'veeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeerylongname'
]

INVALID_TICKET_QUANTITY = ['-50', '101']

INVALID_TICKET_PRICE = ['5', '101']

INVALID_TICKET_DATE = ['January 1 2024', '20243105']

class R5Test(GeekBaseCase):
    '''
    Contains test cases specific to R2
    '''

    def login_test_user(self, *_):
        '''logs in our test user'''

        # Logs user out if there is a session
        self.open(base_url+'/logout')

        # Opens login page
        self.open(base_url+'/login')

        # Inputs test user information into the fields
        self.input('#email', TEST_USER.email)
        self.input('#password', 'Password123!')

        # Submits the inputted information
        self.click('#btn-submit')

        # Opens the user profile page /
        self.open(base_url)

        # Asserts there is a welcome-header id
        self.assert_element('#welcome-header')

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.get_ticket', return_value=TEST_TICKET)
    @patch('qa327.backend.update_ticket', return_value=True)
    def test_r5_1_pos(self, *_):
        '''
        1) (Positive) Test Case R5.1 - The name of the ticket has to be
        alphanumeric-only, and space allowed only if it is not the first or the
        last character.
        '''

        # Logs in user to the server
        self.login_test_user()

        # Inputs previous name for the ticket
        self.input('#update-prev-ticket-name', TEST_TICKET.name)

        # Input updated name for the ticket
        self.input('#update-upt-ticket-name', UPDATED_TEST_TICKET.name)

        # Submit the updated ticket information
        self.click('#update-submit')

        # Verifies that the ticket was successfully updated
        self.assert_flash('User updated ticket successfully')

        # Logs user out the current session
        self.open(base_url+'/logout')


    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.get_ticket', return_value=TEST_TICKET)
    def test_r5_1_neg(self, *_):
        '''
        1) (Negative) Test Case R5.1 - The name of the ticket has to be
        alphanumeric-only, and space allowed only if it is not the first or the
        last character.
        '''

        # Logs in user to the server
        self.login_test_user()

        # Iterates over all of the possible formatting errors for the ticket
        # name including special characters, starting space and ending space.
        for ticket_name in INVALID_TICKET_NAME_FORMATS:
            # Inputs previous name for the ticket
            self.input('#update-prev-ticket-name', TEST_TICKET.name)

            # Input updated name for the ticket
            self.input('#update-upt-ticket-name', ticket_name)

            # Submit the updated ticket information
            self.click('#update-submit')

            # Verifies error message for invalid ticket name format
            self.assert_flash('Ticket name format is incorrect')

        # Logs user out the current session
        self.open(base_url+'/logout')


    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.get_ticket', return_value=TEST_TICKET)
    @patch('qa327.backend.update_ticket', return_value=True)
    def test_r5_2_pos(self, *_):
        '''
        2) (Positive) Test Case R5.2 - The name of the ticket is no longer than
        60 characters.
        '''

        # Logs in user to the server
        self.login_test_user()

        # Inputs previous name for the ticket
        self.input('#update-prev-ticket-name', TEST_TICKET.name)

        # Input updated name for the ticket
        self.input('#update-upt-ticket-name', UPDATED_TEST_TICKET.name)

        # Submit the updated ticket information
        self.click('#update-submit')

        # Verifies that the ticket was successfully updated
        self.assert_flash('User updated ticket successfully')

        # Logs user out the current session
        self.open(base_url+'/logout')


    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.get_ticket', return_value=TEST_TICKET)
    def test_r5_2_neg(self, *_):
        '''
        2) (Negative) Test Case R5.2 - The name of the ticket is no longer than
        60 characters.
        '''

        # Logs in user to the server
        self.login_test_user()

        # Iterates over all of the possible formatting errors for the ticket
        # name length including too short and too long.
        for ticket_name in INVALID_TICKET_NAME_LENGTHS:
            # Inputs previous name for the ticket
            self.input('#update-prev-ticket-name', TEST_TICKET.name)

            # Input updated name for the ticket
            self.input('#update-upt-ticket-name', ticket_name)

            # Submit the updated ticket information
            self.click('#update-submit')

            # Verifies error message for invalid ticket name format
            self.assert_flash('Ticket name format is incorrect')

        # Logs user out the current session
        self.open(base_url+'/logout')


    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.get_ticket', return_value=TEST_TICKET)
    @patch('qa327.backend.update_ticket', return_value=True)
    def test_r5_3_pos(self, *_):
        '''
        3) (Positive) Test Case R5.3 - The quantity of the tickets has to be
        more than 0, and less than or equal to 100.
        '''

        # Logs in user to the server
        self.login_test_user()

        # Inputs previous name for the ticket
        self.input('#update-prev-ticket-name', TEST_TICKET.name)

        # Input updated quantity for the ticket
        self.input('#update-ticket-quantity', UPDATED_TEST_TICKET.quantity)

        # Submit the updated ticket information
        self.click('#update-submit')

        # Verifies that the ticket was successfully updated
        self.assert_flash('User updated ticket successfully')

        # Logs user out the current session
        self.open(base_url+'/logout')


    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.get_ticket', return_value=TEST_TICKET)
    def test_r5_3_neg(self, *_):
        '''
        3) (Negative) Test Case R5.3 - The quantity of the tickets has to be
        more than 0, and less than or equal to 100.
        '''

        # Logs in user to the server
        self.login_test_user()

        # Iterates over all of the possible formatting errors for the ticket
        # quantity including less than 0 and greater than 100.
        for quantity in INVALID_TICKET_QUANTITY:
            # Inputs previous name for the ticket
            self.input('#update-prev-ticket-name', TEST_TICKET.name)

            # Input updated quantity for the ticket
            self.input('#update-ticket-quantity', quantity)

            # Submit the updated ticket information
            self.click('#update-submit')

            # Verifies error message for invalid ticket quantity format
            self.assert_flash('Ticket quantity format is incorrect')

        # Logs user out the current session
        self.open(base_url+'/logout')


    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.get_ticket', return_value=TEST_TICKET)
    @patch('qa327.backend.update_ticket', return_value=True)
    def test_r5_4_pos(self, *_):
        '''
        4) (Positive) Test Case R5.4 - Price has to be of range [10,100]
        '''

        # Logs in user to the server
        self.login_test_user()

        # Inputs previous name for the ticket
        self.input('#update-prev-ticket-name', TEST_TICKET.name)

        # Input updated price for the ticket
        self.input('#update-ticket-quantity', UPDATED_TEST_TICKET.price)

        # Submit the updated ticket information
        self.click('#update-submit')

        # Verifies that the ticket was successfully updated
        self.assert_flash('User updated ticket successfully')

        # Logs user out the current session
        self.open(base_url+'/logout')


    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.get_ticket', return_value=TEST_TICKET)
    def test_r5_4_neg(self, *_):
        '''
        4) (Negative) Test Case R5.4 - Price has to be of range [10,100]
        '''

        # Logs in user to the server
        self.login_test_user()

        # Iterates over all of the possible formatting errors for the ticket
        # price including less than 10 and greater than 100.
        for price in INVALID_TICKET_PRICE:
            # Inputs previous name for the ticket
            self.input('#update-prev-ticket-name', TEST_TICKET.name)

            # Input updated price for the ticket
            self.input('#update-ticket-price', price)

            # Submit the updated ticket information
            self.click('#update-submit')

            # Verifies error message for invalid ticket price format
            self.assert_flash('Ticket price format is incorrect')

        # Logs user out the current session
        self.open(base_url+'/logout')


    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.get_ticket', return_value=TEST_TICKET)
    @patch('qa327.backend.update_ticket', return_value=True)
    def test_r5_5_pos(self, *_):
        '''
        5) (Positive) Test Case R5.5 - Date must be given in the format YYYYMMDD
        '''

        # Logs in user to the server
        self.login_test_user()

        # Inputs previous name for the ticket
        self.input('#update-prev-ticket-name', TEST_TICKET.name)

        # Input updated expiration date for the ticket
        self.input('#update-ticket-expiration-date', UPDATED_TEST_TICKET.expires)

        # Submit the updated ticket information
        self.click('#update-submit')

        # Verifies that the ticket was successfully updated
        self.assert_flash('User updated ticket successfully')

        # Logs user out the current session
        self.open(base_url+'/logout')


    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.get_ticket', return_value=TEST_TICKET)
    def test_r5_5_neg(self, *_):
        '''
        5) (Negative) Test Case R5.5 - Date must be given in the format YYYYMMDD
        '''

        # Logs in user to the server
        self.login_test_user()

        # Iterates over all of the possible formatting errors for the ticket
        # name length including wrong format and invalid date order
        for expires in INVALID_TICKET_DATE:
            # Inputs previous name for the ticket
            self.input('#update-prev-ticket-name', TEST_TICKET.name)

            # Input updated expiration date for the ticket
            self.input('#update-ticket-expiration-date', expires)

            # Submit the updated ticket information
            self.click('#update-submit')

            # Verifies error message for invalid ticket expiration date format
            self.assert_flash('Ticket expiration date format is incorrect')

        # Logs user out the current session
        self.open(base_url+'/logout')


    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.get_ticket', return_value=TEST_TICKET)
    @patch('qa327.backend.update_ticket', return_value=True)
    def test_r5_6_pos(self, *_):
        '''
        6) (Positive) Test Case R5.6 - The ticket of the given name must exist
        '''

        # Logs in user to the server
        self.login_test_user()

        # Inputs previous name for the ticket
        self.input('#update-prev-ticket-name', TEST_TICKET.name)

        # Input updated name for the ticket
        self.input('#update-upt-ticket-name', UPDATED_TEST_TICKET.name)

        # Submit the updated ticket information
        self.click('#update-submit')

        # Verifies that the ticket was successfully updated
        self.assert_flash('User updated ticket successfully')

        # Logs user out the current session
        self.open(base_url+'/logout')


    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.get_ticket', return_value=None)
    def test_r5_6_neg(self, *_):
        '''
        6) (Negative) Test Case R5.6 - The ticket of the given name must exist
        '''

        # Logs in user to the server
        self.login_test_user()

        # Inputs previous name for the ticket that doesn't exist
        self.input('#update-prev-ticket-name', "not_actual_ticket")

        # Input updated name for the ticket
        self.input('#update-upt-ticket-name', "not_update_actual_ticket")

        # Submit the updated ticket information
        self.click('#update-submit')

        # Verifies error message for an invalid ticket submission
        self.assert_flash('Ticket does not exist')

        # Logs user out the current session
        self.open(base_url+'/logout')


    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.get_ticket', return_value=TEST_TICKET)
    @patch('qa327.backend.update_ticket', return_value=True)
    def test_r5_7_pos(self, *_):
        '''
        7) (Positive) Test Case R5.7 - For any errors, redirect back to / and
        show an error message
        '''

        # Logs in user to the server
        self.login_test_user()

        # Inputs previous name for the ticket
        self.input('#update-prev-ticket-name', TEST_TICKET.name)

        # Input updated name for the ticket
        self.input('#update-upt-ticket-name', UPDATED_TEST_TICKET.name)

        # Submit the updated ticket information
        self.click('#update-submit')

        # Verifies that the ticket was successfully updated
        self.assert_flash('User updated ticket successfully')

        # Logs user out the current session
        self.open(base_url+'/logout')


    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.get_ticket', return_value=None)
    def test_r5_7_neg(self, *_):
        '''
        7) (Negative) Test Case R5.7 - For any errors, redirect back to / and
        show an error message
        '''

        # Logs in user to the server
        self.login_test_user()

        # Inputs previous name for the ticket that doesn't exist
        self.input('#update-prev-ticket-name', "not_actual_ticket")

        # Input updated name for the ticket
        self.input('#update-upt-ticket-name', "not_update_actual_ticket")

        # Submit the updated ticket information
        self.click('#update-submit')

        # Verifies error message for an invalid ticket submission
        self.assert_flash('Ticket does not exist')

        # Verifies current URL is the home page
        assert self.get_current_url() == base_url + "/"

        # Logs user out the current session
        self.open(base_url+'/logout')
