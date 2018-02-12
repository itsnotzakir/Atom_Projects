import tweepy
from textblob import TextBlob

consumer_key='Xr43fC06OGrNVUwqZhIQCVzmN'
consumer_secret='R4IOlzbLCbYCNPSSHZngT2bdoEH7XWCQQ2HCSRUUWbbDHUtzAj'

access_token='2550800580-uWq4d1O8p1hFO1Vk3YB6TjBRdIcsuPPefEsVHTS'
acces_token_secret='Phel3Uo2HEMNPMfHm0ClaZGhO86D0lbx4RNReqWr5mP56'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,acces_token_secret)

api=tweepy.API(auth)

public_tweets=api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
