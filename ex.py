from remove_tweets import RemoveTweet

consumer_key = "***"
consumer_secret = "***"
access_token = "***"
access_token_secret = "***"

try:
    remove = RemoveTweet(consumer_key, consumer_secret, access_token, access_token_secret)
    remove.remove_all_tweets("mazlumagar")
except Exception, e:
    print e
