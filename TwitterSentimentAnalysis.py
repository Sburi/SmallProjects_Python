# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 10:38:44 2018

@author: steve
"""

#Purpose
print("This bot analyzes tweets by topic for their general sentiment (positive or negative) subjectivity (fact vs. opinion).\n")

#Tunables
searchTopic = input("What topic would you like to search for on Twitter? ")

#Dependencies
import tweepy
from textblob import TextBlob

#Signin
consumer_key = "4Tc8F1ZcfrY74oljQ8Ibykdll"
consumer_secret = "Gkx8D95KQRCr0pxNeKEsk9mM6jWlereEeeZbwKJKbkzPQVaKAJ"

access_token = "1073961582307229696-gtf4CGFZoRLIIJXz6auWRckeA5PMHY"
access_token_secret = "LUjS5TPw11d27w464PjmyGbPPDGQNF2RGe1RWgL4zFSeT"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Analyze tweets
api = tweepy.API(auth)
public_tweets = api.search(searchTopic)
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("\n")

input("Press enter to close.")



