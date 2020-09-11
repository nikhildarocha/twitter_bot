import os
import tweepy
import time

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
key = os.getenv('api_key')
secret = os.getenv('api_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

hashtag = ("100daysofcode", "Python")
tweetnumber = 5
tweets = tweepy.Cursor(api.search, hashtag).items(tweetnumber)

def search_bot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

   
search_bot()