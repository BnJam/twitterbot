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
import httplib
from random import randint
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

# Autheticating keys
auth_handler = OAuthHandler(C_KEY, C_SECRET)
auth_handler.set_access_token(A_TOKEN, A_TOKEN_SECRET)

# Autheticating client
twitter_client = API(auth_handler, retry_count=1, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


# set logging
logging.getLogger("main").setLevel(logging.INFO)

# exclude these keywords
AVOID = ["java" ]

class PyStreamListener(StreamListener):
	def on_data(self, data):
		while True:
			tweet = json.loads(data)
			try:
				try:
					publish = True

					#if tweet includes excluded words don't retweet
					for word in AVOID:
						if word in tweet['text'].lower():
							logging.info("SKIPPED FOR {}".format(word))
							publish = False

					# if tweet is not in english don't retweet
					if tweet.get('lang') and tweet.get('lang') != 'en':
						publish = False

					# if tweet hasnt been retweeted
					if publish:
						# if new id - retweet
						twitter_client.retweet(tweet['id_str'])
						twitter_client.create_favorite(tweet['id_str'])
						logging.debug("RT: ".format(tweet['text']))
						log("Retweeted: " + tweet['id_str'])
						# sleep for 6 minutes before posting again
						print("Retweeted & Favorited --> Sleeping")
						log("Retweeted & Favorited --> Sleeping")
						#print twitter_client.rate_limit_status()
						time.sleep(60*6)
				# exception handling for failed retweeting		
				except Exception as e:
					logging.error(e)

					# ugly logging of rate limit status
					#log(twitter_client.rate_limit_status())
				return True
			# Handle incomplete reads by continuing to the next target
			except httplib.IncompleteRead:
				print("Incomplete Read occurred --> continuing")
				continue
			except KeyboardInterrupt:
				print("\n\nUser disconnected stream")
				stream.disconnect()
				break
			# exception handling for rate limits	
			except TweepError:
				handle_rate_limit_error()
				print("Rate limit reached --> Sleeping for 1hr")
				log("sleeping")
				time.sleep(60*60)

	def on_error(self, status_code):
		if status_code == 185:
			print("Code 185: User is over daily status update limit --> Sleeping")
			time.sleep(60*15)
			return True
		if status_code == 420:
			# disconnect stream if rate limit is reached
			print("Code 420: Disconnecting stream")
			log("Disconnecting stream")
			time.sleep(60*60)
			print("Retrying stream")
			return True  # return False
		if status_code == 88:
			# disconnect stream if rate limit is reached
			print("Code 88: Rate Limit Exceeded")
			log("Rate Limit Exceeded")
			#time.sleep(60*15)
			#print("Retrying stream")
			return False  # return False
		print status_code


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


# alternate use for message logging
def log(message):
	"""Log message to logfile"""
	path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	with open(os.path.join(path, logfile_name), 'a+') as f:
		t = strftime("%d %b %Y %H:%M:%S", gmtime())
		f.write("\n" + t + " " + str(message))
	
# main execution
if __name__ == "__main__":

	# hashtags to track
	#t = ['#develop', '#coding', '#programming', '#software', '#algorithm', '#bigdata', '#developer']
	# set up random tag to retweet about
	#tag = randint(0,len(t))
	#hashtag = t[tag]
	#print hashtag
	
	listener = PyStreamListener()
	stream = Stream(auth_handler, listener)
	# which hashtags to track and send to stream
	stream.filter(track=['#datascience', '#programming', '#MachineLearning', '#algorithms', '#developer'])
	#print track
