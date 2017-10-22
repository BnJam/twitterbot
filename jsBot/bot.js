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

var params = {q:'#nodejs, #Nodejs, #javascript',
				//result_type: 'recent',
				lang: 'en'}
var params1 = ['#nodejs, #Nodejs, #javascript'];

var Twitter = new twit(config); //Pass in configuration file tokens and such

class JSBot {
	// static retweet - issues finding new tweets
	get retweet() {
		Twitter.get('search/tweets', params, function(err,data) {
			// if there are no errors
			if(!err) {
				//Grab ID of tweet to retweet
				var retweetID = data.statuses[0].id_str;
				console.log(retweetID);
				// Tell Twitter to retweet
				return Twitter.post('statuses/retweet/:id', {
					id: retweetID
				}, function(err, response) {
					if(response) {
						console.log('Retweeted!');
					}
					//if there was an error while tweeting
					if(err) {
						console.log("error while tweeting. "+ err);
					}
					
				});
			} 
			// in unable to search for tweet
			else {
				console.log("Error searching");
			}
		});
	}

	retweet1() {
		var stream = Twitter.stream('statuses/filter', {track:params1});
			stream.on('tweet', function(tweet) {
				//if(params1.valid(tweet)) {
					//if(!params1.debug) {
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
					//} else {
					//	var now = new Date();
					//	console.log('[' + now.toJSON() + '] INVALID: @' + tweet.user.screen_name + ':' + tweet.text);
					//}
				//}
				
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
jsBot.retweet1;

setInterval(jsBot.retweet1,10000);
