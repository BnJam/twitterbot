#!/usr/bin/env python

import os
import tweepy
import json
import logging
import warnings
from pprint import pprint
from tweepy import Stream
from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import API
from secrets import *
from time import gmtime, strftime

warnings.filterwarnings("ignore")

# Individual bot config
# Replace with your bot name
bot_username = 'codingbot1000'
logfile_name = bot_username + ".log"

auth_handler = OAuthHandler(C_KEY, C_SECRET)
auth_handler.set_access_token(A_TOKEN, A_TOKEN_SECRET)

twitter_client = API(auth_handler)

logging.getLogger("main").setLevel(logging.INFO)

AVOID = ["java"]

class PyStreamListener(StreamListener):
	def on_data(self, data):
		tweet = json.loads(data)
		try:
			publish = True
			for word in AVOID:
				if word in tweet['text'].lower():
					logging.info("SKIPPED FOR {}".format(word))
					publish = False
			if tweet.get('lang') and tweet.get('lang') != 'en':
				publish = False
			if publish:
				twitter_client.retweet(tweet['id'])
				logging.debug("RT: {}".format(tweet['text']))
		except Exception as e:
			logging.error(e)
			log(e.message)
		return True

	def on_error(self, status):
		print status


#
#def create_tweet():
#	"""Crease the text of the tweet you want to send"""
	#replace with with custom code
#	text = "My first tweet"
#	return text

#def tweet(text): 
#	"""Send out the text as a tweet"""
	
#	api = tweepy.API(auth)


	# send the tweet and log success or failure
#	try:
#		api.update_status(text)
#	except tweepy.error.TweepError as e:
#		log(e.message)
#	else:
#		log("Tweeted: " + text)



def log(message):
	"""Log message to logfile"""
	path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	with open(os.path.join(path, logfile_name), 'a+') as f:
		t = strftime("%d %b %Y %H:%M:%S", gmtime())
		f.write("\n" + t + " " + str(message))


if __name__ == "__main__":
#	tweet_text = create_tweet()
#	tweet(tweet_text)
	listener = PyStreamListener()
	stream = Stream(auth_handler, listener)
	stream.filter(track=['#code','#coding','#programming'])