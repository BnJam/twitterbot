// bot.js
// Author: Benjamin Smith // BnJam

/*
 Retweet bot that retweets based on passed tags
*/

var twit = require('twit');
var config = require('./config.js');
var sleep = require('sleep');
var flag = 0;
var now = new Date();

var params = {
	q: '#nodejs, #Nodejs, #javascript',
	result_type: 'recent',
	lang:'en'
}

var Twitter = new twit(config); //Pass in configuration file tokens and such

class JSBot {
	
	// Retweets a tweet based on the tracked tags.
	retweet() {
		// Post retweet
			
		Twitter.get('search/tweets', params, function(err, data) {
			if(err) {
				console.log('Something went wrong when searching...');
			} else {
				var retweetId = data.statuses[0].id_str;
				Twitter.post('statuses/retweet/:id', {id: retweetId}, function(err, response) {
					if(err) {
						console.log(err);
					} else {
						console.log("Retweeted!");
						console.log('[' + now.toJSON() + '] SENT: ' + response);
					}
				});
				Twitter.post('favorites/create', {id: retweetId}, function(err, reply) {
					if(err) {
						console.log(err);
					} else {
						console.log("Favorited!");
						console.log('[' + now.toJSON() + '] FAVORITED: ' + reply);
					}
				});
			}
		});
	}
}

var jsBot = new JSBot();


jsBot.retweet;


setInterval(jsBot.retweet,15*6000); // 
