import tweepy

def get_api(KEY1, KEY2, KEY3, KEY4):
  auth = tweepy.OAuthHandler(KEY1, KEY2)
  auth.set_access_token(KEY3, KEY4)
  return tweepy.API(auth)

def tweet_message(KEY1, KEY2, KEY3, KEY4, msg):
  api = get_api(KEY1, KEY2, KEY3, KEY4)
  status = api.update_status(status = msg)
  return "Done"
