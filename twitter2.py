# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 22:34:39 2018

@author: Mik
"""

import tweepy

# Copy the api key, the api secret, the access token and the access token secret from the relevant page on your Twitter app 

api_key = 'qHZggTyRM9J0rE3lJkV0APoU8'
api_secret = 'fvbbowrxh81SrmbQ3li98ddylU5HecpVxqhxjLQbyzfJYn2vhr'
access_token = '141720522-21so0YHS0uuEYIzx4m4DwPdcbtz6fek9DiKsglfT'
access_token_secret = '2OwbvymwBmfkureUacIcMIAFuZNH4DUMyxrOuMOv6FfpH'
# You don't need to make any changes below here # This bit authorises you to ask for information from Twitter 
auth = tweepy.OAuthHandler(api_key, api_secret) 
auth.set_access_token(access_token, access_token_secret) 
# The api object gives you access to all of the http calls that Twitter accepts 
api = tweepy.API(auth) 

#User we want to use as initial node 
user='TheOpenBacteria'

import csv 
import time 
#This creates a csv file and defines that each new entry will be in a new line 
csvfile=open(user+'network2.csv', 'w') 
spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL) 
#This is the function that takes a node (user) and looks for all its followers #and print them into a CSV file... and look for the followers of each follower... 

def fib(n,user,spamwriter):
    if n>0:
        #There is a limit to the traffic you can have with the API, so you need to wait 
        #a few seconds per call or after a few calls it will restrict your traffic 
        #for 15 minutes. This parameter can be tweeked 
        time.sleep(40) 
        try:
            users=tweepy.Cursor(api.followers, screen_name = user, wait_on_rate_limit = True).items()
            for follower in users:
                print(follower.screen_name)
                spamwriter.writerow([user+';'+follower.screen_name]) 
                fib(n-1,follower.screen_name,spamwriter) 
                #n defines the level of autorecurrence

        except tweepy.TweepError:
                print("Failed to run the command on that user, Skipping...")
            

n=1
fib(n,user,spamwriter)