def twitter_error():
    print("""It seems you haven't yet created the twitter app to post messages. To create your own app, go to https://apps.twitter.com/
    and create a developer account, and after that go to https://developer.twitter.com/en/apps and create an app by entering the details about your app, after creating the app you will get 4 authorisation keys namely consumer API key, consumer secret API key, access token and access token secret key, and enter them below""")
    consumer_api_key = input("Consumer API Key: ")
    consumer_secret_key = input("Consumer secret API Key: ")
    access_token = input("Access token key: ")
    access_token_secret = input("Access token secret key: ")
    print("please broadcast the message again")
    return consumer_api_key, consumer_secret_key, access_token, access_token_secret
