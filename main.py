import tweepy
import requests
consumer_key = ''
consumer_secret = ''
access_token = ""
access_token_secret = ""
client = tweepy.Client(consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret)
response = client.create_tweet(text='hello world')
