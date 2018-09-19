import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  
  api = get_api(cfg)
  tweet = "Hi, This is Nipun!"
  status = api.update_status(tweet) 

if __name__ == "__main__":
  main()
