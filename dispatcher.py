import error_twitter
import broadcaster_twitter
import dict2json
global loaded_config

def load_config():
    wrapper = open("./config.json", "r+")
    data = wrapper.readline()
    global loaded_config
    loaded_map = json.loads(data)
    return loaded_config

def twitter_broadcast(KEY1, KEY2, KEY3, KEY4, message):
    broadcaster_twitter.tweet_message(KEY1, KEY2, KEY3, KEY4, message)
    
def main(message):
    load_config()
    if config['twitter']:
        twitter_broadcast(config['twitter']['KEY1'], config['twitter']['KEY2'], config['twitter']['KEY3'], config['twitter']['KEY4'], message)
    else:
         KEY1, KEY2, KEY3, KEY4 = error_twitter.twitter_error()
         dict2json.store_twitter_creds(KEY1, KEY2, KEY3, KEY4)

        
    
