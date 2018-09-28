import broadcast
import pytest
from unittest.mock import patch
import sys

def test_return_cmdline_message():
    testargs = ["broadcast", "hi"]
    with patch.object(sys, 'argv', testargs):
        assert broadcast.return_msg_from_cmdline() == "hi"
