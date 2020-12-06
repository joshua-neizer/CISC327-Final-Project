from unittest.mock import patch

from qa327_test.conftest import base_url
from qa327_test.frontend.geek_base import GeekBaseCase, TEST_USER
from qa327.models import Ticket
from qa327.ticket_format import parse_date

#@patch('qa327.backend.get_all_tickets', return_value = TEST_TIX)