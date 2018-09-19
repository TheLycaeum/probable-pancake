import json
dictio = {}
def store_twitter_creds(KEY1, KEY2, KEY3, KEY4):
    dictio['twitter']={
        'KEY1': KEY1,
        'KEY2': KEY2,
        'KEY3': KEY3,
        'KEY4': KEY4
     }
    dumped_dictio = json.dumps(dictio)
    loaded_dictio = json.loads(dumped_dictio)
    
    with open('config.json', 'w') as outfile:
        json.dump(loaded_dictio, outfile)
        
    outfile.close()

def clear_config_file():
    empty_dict = {}
    dumped_dictio = json.dumps(empty_dict)
    loaded_dictio = json.loads(dumped_dictio)
    
    with open('config.json', 'w') as outfile:
        json.dump(loaded_dictio, outfile)
        
    outfile.close()
