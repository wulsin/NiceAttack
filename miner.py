#!/usr/bin/env python

import json 
import tweepy
from tweepy import OAuthHandler
import config 

auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)
  
api = tweepy.API(auth)

def process_or_store(tweet):
    print(json.dumps(tweet))

# for status in tweepy.Cursor(api.home_timeline).items(10):
#     # Process a single status
#     print(status.text) 

# for status in tweepy.Cursor(api.home_timeline).items(3):
#     # Process a single status
#     process_or_store(status._json) 

# for friend in tweepy.Cursor(api.friends).items():
#     process_or_store(friend._json)

for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)

print "done"



