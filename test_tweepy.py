from unittest.mock import Mock
import broadcaster_twitter
import pytest


def test_tweepy_get_api():
    
    mock_api = Mock(return_value = "Hello world!")

    original_req = broadcaster_twitter.tweepy.API
    broadcaster_twitter.tweepy.API = mock_api

    KEY1 = ""
    KEY2 = ""
    KEY3 = ""
    KEY4 = ""
    
    
    api = broadcaster_twitter.get_api(KEY1, KEY2, KEY3, KEY4)
    assert api == "Hello world!"
    broadcaster_twitter.tweepy.API = original_req

def test_tweet_message():
    KEY1 = ""
    KEY2 = ""
    KEY3 = ""
    KEY4 = ""
    msg = "something testing"

    mock_tweet_message = Mock()
    mock_tweet_message.tweet_message = Mock(return_value = "Done")
    
    original_req = broadcaster_twitter.tweet_message
    broadcaster_twitter.tweet_message = mock_tweet_message.tweet_message

    
    assert broadcaster_twitter.tweet_message(KEY1, KEY2, KEY3, KEY4, msg) == "Done"
