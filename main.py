import tweepy
import os
from datetime import date
from datetime import timedelta
from json import dumps
consumer_key = os.environ['TWITTER_API_KEY']
consumer_secret = os.environ['TWITTER_API_SECRET_KEY']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
client = tweepy.Client(consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret)
days = date(2024,9,27) - date.today() - timedelta(days = 1)
cd = dumps(days.days, default=str)
response = client.create_tweet(text=cd)
