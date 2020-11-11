import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch

class Http404Test(BaseCase):

    def test_404_text(self, *_):
        # open home page
        self.open(base_url+'/randomtest')
        # test if the page loads correctly
        self.assert_element('#error404')