import os
import tweepy
from secrets import *
from time import gmtime, strftime

# individual bot config
bot_username = 'codingbot1000'
logfile_name = bot_username + ".log"

#

def create_tweet():
	"""Crease the text of the tweet you want to send"""
	#replace with with custom code
	text = ""
	return text

def tweet(text): 
	"""Send out the text as a tweet"""
	auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
	auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
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
		f.write("\n" + t + " " + message)


if __name__ == "__main__":
	tweet_text = create_tweet()
	tweet(tweet_text)