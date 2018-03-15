#!/usr/bin/env python

# Author: Benjamin Smith
# Date:   6th Feb 2017
# File: bot.py
# Purpose: Retweet tweets associated toward computer science topics

# import libraries
import os
import tweepy 
import json
import logging
import warnings
import time
import http.client
from secrets import *
from time import gmtime, strftime

warnings.filterwarnings("ignore")

# Individual bot config
# Replace with your bot name
bot_username = 'codingbot1000'
logfile_name = bot_username + ".log"

# Autheticating keys
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)

api = tweepy.API(auth)


# set logging
logging.getLogger("main").setLevel(logging.INFO)

# exclude these keywords
AVOID = ["java" ]

hashtags = ['#python','#developer','#py']

class pyBot:
	print("pyBotv2")
	def re_tweet(self):
		try:
			for tweet in tweepy.Cursor(api.search,q='#python').items(200):
				print("Retweet by: @" + tweet.user.screen_name)
				tweet.retweet()
				print("Retweeted: " + tweet.id_str)
				tweet.favorite()
				print("Sleeping for 5 mins...")
				time.sleep(5*60)
		except tweepy.TweepError as e:
			print(e.reason)
		except StopIteration:
			return

if __name__ == "__main__":
	pybot = pyBot()
	pybot.re_tweet()