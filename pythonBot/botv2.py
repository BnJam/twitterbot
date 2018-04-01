#!/usr/bin/env python

# Author: Benjamin Smith
# Date:   March 14 2018
# File: botv2.py
# Purpose: Retweet tweets associated with Python

# import libraries
import os
import tweepy 
import json
import csv
import warnings
import time
import http.client
from secrets import *
from time import gmtime, strftime

warnings.filterwarnings("ignore")

# Individual bot config
# Replace with your bot name
bot_username = '@codingbot1000'
logfile_name = bot_username + ".log"

# Autheticating keys
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)

api = tweepy.API(auth)

# open csv for data collection
header = ["User_ID", "Username", "Date", "Tweet_ID"]


# exclude these keywords
AVOID = ["java" ]

q = ['#python','#developer','#py']

class pyBot:
	print("pyBotv2")

	def re_tweet(self):
		try:
			with open("botv2.csv", 'a') as datalog:
				writer = csv.writer(datalog, delimiter=',')
				for tweet in tweepy.Cursor(api.search,q='#python', lang='en').items(1000):
					if(tweet.user.screen_name == bot_username):
						pass
					else:
						ht = []
						for hashtag in tweet.entities['hashtags']:
							ht.append(hashtag['text'])
						if(tweet.retweet()):
							writer.writerow([tweet.user.id_str, tweet.user.screen_name, tweet.created_at, tweet.id_str, ht])
							print("Retweet by: @" + tweet.user.screen_name)
							print("Retweeted: " + tweet.id_str)
							tweet.favorite()
							print("Favorited: " + tweet.id_str)
							print("Sleeping for 2 mins...")
							time.sleep(2*60)
						else:
							print("Already retweeted...")
							continue
		except tweepy.TweepError as e:
			print("Error Thrown: "+ e.reason)
			pass
		except StopIteration:
			print("StopIteration")



if __name__ == "__main__":
	pybot = pyBot()
	pybot.re_tweet()