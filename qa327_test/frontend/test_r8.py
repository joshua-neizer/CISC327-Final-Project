from unittest.mock import patch
from seleniumbase import BaseCase

from qa327_test.frontend.geek_base import GeekBaseCase
from qa327_test.conftest import base_url

class R8Test(GeekBaseCase):
    '''
    contains test cases for R8 requirements
    '''

    def test_404_text(self, *_):
        '''
        verifies that our 404 page is actually displayed
        '''
        # open home page
        self.open(base_url+'/randomtest')
        # test if the page loads correctly
        self.assert_element('#error404')