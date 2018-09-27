from unittest.mock import Mock
import broadcaster_twitter
import pytest


def test_tweepy():
    mock = Mock()
    # mock.API = "Hello world!"
    mock_api = Mock(return_value = "Hello world!")
    original_req = broadcaster_twitter.tweepy.API
    broadcaster_twitter.tweepy.API = mock_api

    KEY1 = ""
    KEY2 = ""
    KEY3 = ""
    KEY4 = ""

    
    api = broadcaster_twitter.get_api(KEY1, KEY2, KEY3, KEY4)
    assert api == "Hello world!"
