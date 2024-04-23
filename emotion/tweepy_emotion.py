# import tweepy
# from tweepy import OAuthHandler
# from tweepy import API
# from tweepy import Cursor
# from datetime import datetime, date, time, timedelta
# from collections import Counter
# import sys
# import numpy as np
# import pandas as pd

# class Import_tweet_emotion:

# 	# consumer_key="user consumer_key"
# 	# consumer_secret="user consumer_secret"
# 	# access_token="user access_token"
# 	# access_token_secret="user access_token_secret"
# 	# consumer_key="uLgirpmLFyvvSnM7x1MMeFuK6"
# 	# consumer_secret="zRUGtDZXVwXbZgj9GTtC1IYoqHFfraGT9UsRvyo4qP6o7XcW5R"
# 	# access_token="1164005014915944448-4uYfxygKAPI0MYiSD0zEJkk6VTfJpl"
# 	# access_token_secret="bqoA2XIsJwX4pHj6Vs3jBP8DaR1Yylb4HSvL78Ub0fpDz"


# 	def tweet_to_data_frame(self,tweets):
# 		tweets=["i am sad", "i am good"]
# 		df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
# 		return df

# 	def get_tweets(self, handle):
# 		# auth = OAuthHandler(self.consumer_key, self.consumer_secret)
# 		# auth.set_access_token(self.access_token, self.access_token_secret)
# 		# auth_api = API(auth)

# 		# account = handle
# 		item = ["i am sad", "i am good"]
# 		df = self.tweet_to_data_frame(item)

# 		all_tweets = []
# 		for j in range(20):
# 			all_tweets.append(df.loc[j]['Tweets'])
# 		return all_tweets

# 	def get_hashtag(self, hashtag):
# 		# auth = OAuthHandler(self.consumer_key, self.consumer_secret)
# 		# auth.set_access_token(self.access_token, self.access_token_secret)
# 		# auth_api = API(auth)

# 		# account = hashtag
# 		# all_tweets = []
#         #  all_tweets = ["i am sad", "i am good"]
# 		# for tweet in tweepy.Cursor(auth_api.search, q=account, lang='en').items(20):
# 		# 	all_tweets.append(tweet.text)

#          return ""

from textblob import TextBlob

class Import_tweet_emotion:
    def get_tweets(self, sentence):
        # sentence="I am very good"
        blob = TextBlob(sentence)
        sentiment = blob.sentiment.polarity

        if sentiment > 0.3:
            return "Love"
        elif sentiment > 0:
            return "Happiness"
        elif sentiment < -0.3:
            return "Sadness"
        elif sentiment < 0:
            return "Worry"
        else:
            return "Happiness"
    def get_hashtag_naredaramodi(self, sentence):
        return ["Team at AIIMSNagpur on this feat, setting a benchmark in delivering quality healthcare services.", "Birthday wishes to Health Minister @mansukhmandviya Ji. He is making innumerable efforts to improve India’s health infrastructure and ensuring that the poor have top quality and affordable healthcare. Praying for his long and healthy life.","The 2022-23 GDP growth figures underscore the resilience of the Indian economy amidst global challenges. This robust performance along with overall optimism and compelling macro-economic indicators, exemplify the promising trajectory of our economy and the tenacity of our people.","Saddened by the passing away of Lok Sabha MP from Chandrapur, Shri Balubhau Narayanrao Dhanorkar Ji. He will be remembered for his contribution to public service and empowering the poor. Condolences to his family and supporters. Om Shanti."]   
    

# Example usage
# detector = Import_tweet_emotion()
# sentence1 = "I am very sad"
# sentence2 = "I feel worried about the upcoming exam"
# emotion1 = detector.detect_emotion(sentence1)
# emotion2 = detector.detect_emotion(sentence2)
# print("Emotion for sentence 1:", emotion1)
# print("Emotion for sentence 2:", emotion2)
