from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import tweepy
import numpy as np
import pandas as pd

class Import_tweet_sentiment:

	# consumer_key="user consumer_key"
	# consumer_secret="user consumer_secret"
	# access_token="user access_token"
	# access_token_secret="user access_token_secret"
	# consumer_key = "uLgirpmLFyvvSnM7x1MMeFuK6"
    # consumer_secret = "zRUGtDZXVwXbZgj9GTtC1IYoqHFfraGT9UsRvyo4qP6o7XcW5R"
    # access_token = "1164005014915944448-4uYfxygKAPI0MYiSD0zEJkk6VTfJpl"
    # access_token_secret = "bqoA2XIsJwX4pHj6Vs3jBP8DaR1Yylb4HSvL78Ub0fpDz"
	consumer_key="uLgirpmLFyvvSnM7x1MMeFuK6"
	consumer_secret="zRUGtDZXVwXbZgj9GTtC1IYoqHFfraGT9UsRvyo4qP6o7XcW5R"
	access_token="1164005014915944448-4uYfxygKAPI0MYiSD0zEJkk6VTfJpl"
	access_token_secret="bqoA2XIsJwX4pHj6Vs3jBP8DaR1Yylb4HSvL78Ub0fpDz"
 
	def tweet_to_data_frame(self, tweets):
		df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
		return df

	def get_tweets(self, handle):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		auth_api = API(auth)

		account = handle
		item = auth_api.user_timeline(id=account,count=20)
		df = self.tweet_to_data_frame(item)

		all_tweets = []
		for j in range(20):
			all_tweets.append(df.loc[j]['Tweets'])
		return all_tweets

	def get_hashtag(self, hashtag):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		auth_api = API(auth)

		account = hashtag
		all_tweets = []

		for tweet in tweepy.Cursor(auth_api.search, q=account, lang='en').items(20):
			all_tweets.append(tweet.text)

		return all_tweets
