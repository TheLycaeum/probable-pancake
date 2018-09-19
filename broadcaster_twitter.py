import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  
  cfg = { 
    "consumer_key"        : "M8VYWKswCUQW7EqnzeabStIXf",
    "consumer_secret"     : "v0p7rsJNAddbRu1SKebvrj7b9wtTs3C5aMWCychBxB2MZWaMoS",
    "access_token"        : "201037788-ScByvRNzOiCbGIhvATmqszz9hfHwhKx5B0dFHki1",
    "access_token_secret" : "5QEbE3SCpxrIXEDXFshe7aU7DTEEjznxlos2GQ00POf6l" 
    }

  api = get_api(cfg)
  tweet = "Hi, This is Nipun!"
  status = api.update_status(tweet) 

if __name__ == "__main__":
  main()
