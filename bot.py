#!/usr/bin/env python

import os
import tweepy
import ConfigParser
import inspect
import hashlib
from tweepy import Stream
from tweepy import StreamListener
from tweepy import OAuthHandler
from secrets import *
from time import gmtime, strftime

# Individual bot config
# Replace with your bot name
bot_username = 'codingbot1000'
logfile_name = bot_username + ".log"

auth = OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)

#class TweetListener(StreamListener):
#	def on_status(self, status):
#		print "tweet" + str(status.created_at) + "\n"
#		print status.ext + "\n"
#stream = Stream(auth, TweetListener(), secure=True, )
#t = u"#code" + u"coding" + u"#programming"
#stream.filter(track=[t])

#
def create_tweet():
	"""Crease the text of the tweet you want to send"""
	#replace with with custom code
	text = "My first tweet"
	return text

def tweet(text): 
	"""Send out the text as a tweet"""
	
	api = tweepy.API(auth)


	# send the tweet and log success or failure
	try:
		api.update_status(text)
	except tweepy.error.TweepError as e:
		log(e.message)
	else:
		log("Tweeted: " + text)



def log(message):
	"""Log message to logfile"""
	path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	with open(os.path.join(path, logfile_name), 'a+') as f:
		t = strftime("%d %b %Y %H:%M:%S", gmtime())
		f.write("\n" + t + " " + str(message))


if __name__ == "__main__":
	tweet_text = create_tweet()
	tweet(tweet_text)