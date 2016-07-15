#!/usr/bin/env python

import json 
import tweepy
from tweepy import OAuthHandler
import config 
import os 
 
auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)
 
api = tweepy.API(auth)

def process_or_store(tweet):
    print(json.dumps(tweet))

from tweepy import Stream
from tweepy.streaming import StreamListener
 
onlyTimeStamps = True

fname = 'python.json'
if onlyTimeStamps:
    fname = 'timestamps.txt'
    
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open(fname, 'a') as f:                
                if onlyTimeStamps:
                    # print json.loads(data)['created_at']  
                    f.write(json.loads(data)['created_at'] + "\n")  
                else:
                    f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 

if os.path.isfile(fname):
    os.remove(fname) 
twitter_stream = Stream(auth, MyListener())
#twitter_stream.filter(track=['#python'])    # Very slow rate
#twitter_stream.filter(track=['#BlackLivesMatter'])  # Fast rate:  ~1 Hz
#twitter_stream.filter(track=['#NiceAttack'])   # Very fast:  ~20 Hz
twitter_stream.filter(track=['#Nice'])   # Very fast:  ~20 Hz

print "done"



