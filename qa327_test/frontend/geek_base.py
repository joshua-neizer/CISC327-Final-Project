from seleniumbase import BaseCase
from werkzeug.security import generate_password_hash
from qa327_test.conftest import base_url
from qa327.models import User

# Mock a sample user
TEST_USER = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend'),
    balance=140
)

class GeekBaseCase(BaseCase):
    '''
    Selenium base case with some
    GeekSeek utilities
    '''

    def assert_flash(self, text):
        '''asserts that message exists in flashes'''
        for flash_dom in self.find_elements('.flash'):
            if flash_dom.text == text:
                return
        raise AssertionError(f'Flash not found for text "{text}"')

    def login_test_user(self, email=TEST_USER.email, password='test_frontend'):
        '''login our test user'''
        self.open(base_url+'/login')
        self.input('#email', email)
        self.input('#password', password)
        self.click('#btn-submit')