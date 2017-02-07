#!/usr/bin/env python

# import libraries
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

# Autheticating keys
auth_handler = OAuthHandler(C_KEY, C_SECRET)
auth_handler.set_access_token(A_TOKEN, A_TOKEN_SECRET)

# Autheticating client
twitter_client = API(auth_handler)

# set logging
logging.getLogger("main").setLevel(logging.INFO)

# exclude these keywords
AVOID = ["java" ]


class PyStreamListener(StreamListener):
	def on_data(self, data):
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
					logging.debug("RT: {}".format(tweet['text']))
					log("Retweeted: " + tweet['id_str'])
					#print twitter_client.rate_limit_status()
			# exception handling for failed retweeting		
			except Exception as e:
				logging.error(e)
				#log(e.message)

				# ugly logging of rate limit status
				#log(twitter_client.rate_limit_status())
			return True

		# exception handling for rate limits	
		except TweepError:
			handle_rate_limit_error()
			log("sleeping")
			time.sleep(60*15)

	def on_error(self, status):
		if status == 420:
			# disconnect stream if rate limit is reached
			log("Disconnecting stream")
			return False
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


# alternate use for message logging
def log(message):
	"""Log message to logfile"""
	path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	with open(os.path.join(path, logfile_name), 'a+') as f:
		t = strftime("%d %b %Y %H:%M:%S", gmtime())
		f.write("\n" + t + " " + str(message))


# main execution
if __name__ == "__main__":
	listener = PyStreamListener()
	stream = Stream(auth_handler, listener)
	# which hashtags to track and send to stream
	stream.filter(track=['#develop', '#coding', '#programming', '#computerscience', '#compsci', '#softwaredeveloper', '#software', '#algorithm', '#bigdata'])
