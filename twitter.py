import tweepy
from time import sleep
from os import environ

consumer_key = environ['CONSUMER_KEY']
consumer_key_secret = environ['CONSUMER_KEY_SECRET']
access_token = environ['ACCESS_TOKEN']
access_token_secret = environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

with open("tweet_id", 'r') as file:
    tweet_id = file.read()

def likes():
    tweet = api.get_status(tweet_id)
    likes = tweet.favorite_count
    return likes

def retweets():
    tweet = api.get_status(tweet_id)
    retweet = tweet.retweet_count
    return retweet

previous_like = ""
previous_retweet = ""

while True:
    like = str((likes()))
    retweet = str((retweets()))
    if like != previous_like or retweet != previous_retweet:
        previous_like = like
        previous_retweet = retweet
        bio = "Likes: " + like + ", Retweet: " + retweet
        api.update_profile(description=bio)
    else:
        pass
    sleep(5)