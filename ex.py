import remove_tweets

consumer_key = "***"
consumer_secret = "***"
access_token = "***"
access_token_secret = "***"

remove = remove_tweets.RemoveTweet(consumer_key, consumer_secret, access_token, access_token_secret)
remove.remove_all_tweets("mazlumagar")

