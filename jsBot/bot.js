// bot.js
// Author: Benjamin Smith // BnJam
// 
// References:
// https://hackernoon.com/create-a-simple-twitter-bot-with-node-js-5b14eb006c08



var twit = require('twit');
var config = require('./config.js');
var sleep = require('sleep');
var flag = 0;
var now = new Date();

var params = ['#nodejs, #Nodejs, #javascript'];

var Twitter = new twit(config); //Pass in configuration file tokens and such

class JSBot {
	
	// Retweets a tweet based on the tracked tags.
	retweet() {
		var stream = Twitter.stream('statuses/filter', {track:params});
			stream.on('tweet', function(tweet) {
				
				// Post retweet
				Twitter.post('statuses/retweet', {id: tweet.id_str}, function(err, reply) {
					if(err) {
						console.log(err);
					} else {
						if(flag == 0) {
							console.log('[' + now.toJSON() + '] SENT: ' + tweet.text);
							console.log("Sleeping for 4 mins at " + now.toJSON());
							sleep.sleep(240); // 4 mins
						}
						if(flag == 1) {
							console.log('[' + now.toJSON() + '] SENT: ' + tweet.text);
							console.log("Sleeping for 10 mins at " + now.toJSON());
							sleep.sleep(600); // 10 mins
						}
						if(flag == 2) {
							console.log('[' + now.toJSON() + '] SENT: ' + tweet.text);
							console.log("Sleeping for 8 mins at " + now.toJSON());
							sleep.sleep(480); // 8 mins
						}
						if(flag == 3) {
							console.log('[' + now.toJSON() + '] SENT: ' + tweet.text);
							console.log("Sleeping for 12 mins at " + now.toJSON());
							sleep.sleep(720);
						}
					}
				});
			});
		if(flag == 3) {
			flag = 0;
		} else {
			flag++;
		}
		return stream;
	}
}

var jsBot = new JSBot();
jsBot.retweet;

setInterval(jsBot.retweet,10000);
