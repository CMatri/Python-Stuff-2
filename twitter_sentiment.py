import tweepy
from textblob import TextBlob

consumer_key = 'MTyOQJxyriiUz7IYTygjhGdlg'
consumer_secret = 'Bg4SoOGSFrEqzZJWZB22sOSRamIp1Y9GlSwxUnWJ6JKt1inU91'
access_token = '1352751529-nTThQ9vWndKxKWlVxnXA4iGxNdkVVR7FnOM72Oi'
access_token_secret = '5L8Tl3zp4WDvuKcwP7NYhtgF9QxCWNltsyTng9inMAQDk'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('beautiful')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment, '\n')
