import tweepy

consumer_key = 'N7nYQv7iDQutsN0XOMTW47l1R'
consumer_key_secret = 'rLZMF2wjShshiLkT5SO5dsA5XYCnklrVvZym3UuLbzrtewGT7J'
access_token = '1058371167482916866-MhtUsgycQYmf39uPFgYvPOgsbtjj4j'
access_token_secret = 'Ld2Dnfqt96ClUgCXAj3psuDCTDxmKdR7LQSYk51o9GA4o'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)