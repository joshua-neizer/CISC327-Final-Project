import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch

class R3Test(BaseCase):

    def test_login_redirects(self, *_):
        '''
        see r3.1
        '''
        # open home page
        self.open(base_url)
        # verify redirected to /login
        assert self.get_current_url() == base_url+'/login'
        self.assert_element('#login_input')