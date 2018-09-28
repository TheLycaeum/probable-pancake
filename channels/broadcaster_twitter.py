import tweepy
global api
def get_api(KEY1, KEY2, KEY3, KEY4):
  auth = tweepy.OAuthHandler(KEY1, KEY2)
  auth.set_access_token(KEY3, KEY4)
  global api
  api = tweepy.API(auth)
  return api

def tweet_message(api, msg):
  status = api.update_status(status = msg)
  return "Done"


# class TwitterChannel:
#   def __init__(self, k1, k2, k3, k4):
#     auth = tweepy.OAuthHandler(k1, k2)
#     auth.set_access_token(k3, k4)
#     self.api = tweepy.API(auth)

#   def send_message(self, message):
#     self.api.update_status(status = message)



# ch = TwitterChannel('', '', '', '')
# ch.send_message("Hello world")
    
