import error_twitter
from channels import broadcaster_twitter
import dict2json
import json
global loaded_config
import sys
import os
from os import listdir
from os.path import isfile, join


def load_config():
    try:
        wrapper = open("./config.json", "r+")
        data = wrapper.readline()
        global loaded_config
        loaded_config = json.loads(data)
        return loaded_config
    except:
        dict2json.clear_config_file()
        wrapper = open("./config.json", "r+")
        data = wrapper.readline()
        loaded_config = json.loads(data)
        return loaded_config


def file_list():
    mypath = os.getcwd() + '/channels'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles


def twitter_broadcast(KEY1, KEY2, KEY3, KEY4, message):
    broadcaster_twitter.tweet_message(KEY1, KEY2, KEY3, KEY4, message)
    
def main(message):
    load_config()
    if 'twitter' in loaded_config:
        twitter_broadcast(loaded_config['twitter']['KEY1'], loaded_config['twitter']['KEY2'], loaded_config['twitter']['KEY3'], loaded_config['twitter']['KEY4'], message)
    else:
         KEY1, KEY2, KEY3, KEY4 = error_twitter.twitter_error()
         dict2json.store_twitter_creds(KEY1, KEY2, KEY3, KEY4)

        
    
