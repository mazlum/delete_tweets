import tweepy
#This class to delete automatically tweets


class RemoveTweet:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    #This method removes tweets as count
    def remove_tweets(self, username, count):
        if raw_input("Are you sure for remove tweets? [yes/no]") != "yes":
            return False
        if not count > 200:
            last_tweets = self.api.user_timeline(screen_name=username, count=count)
        else:
            last_tweets = self.api.user_timeline(screen_name=username, count=200)
            oldest_id = last_tweets[-1].id - 1
        while True:
            count -= 200
            for tweet in last_tweets:
                print tweet.text
                self.api.destroy_status(tweet.id)
            if count < 0:
                break
            elif count > 200:
                last_tweets = self.api.user_timeline(screen_name=username, count=200, max_id=oldest_id)
            else:
                last_tweets = self.api.user_timeline(screen_name=username, count=count % 200, max_id=oldest_id)

            if len(last_tweets) > 0:
                oldest_id = last_tweets[-1].id - 1
            else:
                break

    #This method removes all tweets.
    def remove_all_tweets(self, username):
        if raw_input("Are you sure for remove all tweets? [yes/no]") != "yes":
            return False
        #Twitter allows take a maximum 200 tweet a once
        last_tweets = self.api.user_timeline(screen_name=username, count=200)
        oldest_id = last_tweets[-1].id - 1
        while True:
            for tweet in last_tweets:
                #remove tweet
                self.api.destroy_status(tweet.id)
            #take next 200 tweet
            last_tweets = self.api.user_timeline(screen_name=username, count=200, max_id=oldest_id)
            if len(last_tweets) > 0:
                oldest_id = last_tweets[-1].id - 1
            else:
                break

