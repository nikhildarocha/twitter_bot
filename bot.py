import tweepy
import time

consumer_key = 'Hq6m9WM7gwt1wPYZ2PZFeJFXV'
consumer_secret = '9Y7XNfNTU9GLZpEMOMste4MQLlliFaQvHV3kIJg8u8BDYhzgmu'
key = '1216427695673790465-ErMuJ1qdl5MzWEah8knf6Z1RGR9q3B'
secret = '8jlzHWuWwYkkhCM2s3sIAQwcYLqUJ6AHA9m0pCIYFdjAJ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)


FILE_NAME = 'last_seen.txt'


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id



def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#randomtweet' in tweet.full_text.lower():
            print("Replied to ID" + str(tweet.id))
            api.update_status("@" + tweet.user.screen_name + " Hello", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)
    


while True:
    reply()
    time.sleep(15)
    