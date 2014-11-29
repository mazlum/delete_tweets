import tweepy
#This class delete automatically


class RemoveTweet:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        #authorize twitter
        try:
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(auth)
        except Exception, e:
            print "Error: We can't connect twitter. Check your credentials."

    #This method removes tweets as count
    def remove_tweets(self, username, count):
        if raw_input("Are you sure for remove tweets? [yes/no]") != "yes":
            return False
        try:
            if not count > 200:
                last_tweets = self.api.user_timeline(screen_name=username, count=count)
            else:
                last_tweets = self.api.user_timeline(screen_name=username, count=200)
                oldest_id = last_tweets[-1].id - 1
        except Exception, e:
            print "Error: We can't take your tweets."
            return False

        while True:
            try:
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

            except Exception, e:
                print "Error: We can't take your tweets."
                return False

    #This method removes all tweets.
    def remove_all_tweets(self, username):
        if raw_input("Are you sure for remove all tweets? [yes/no]") != "yes":
            return False
        try:
            #Twitter allows take a maximum 200 tweet a once
            last_tweets = self.api.user_timeline(screen_name=username, count=200)
            #get last tweet id
            oldest_id = last_tweets[-1].id - 1
        except Exception, e:
            print "Error: We can't take your tweets."
            return False
        while True:
            try:
                for tweet in last_tweets:
                    #remove tweet
                    print tweet.text
                    #self.api.destroy_status(tweet.id)
                #take next 200 tweet
                last_tweets = self.api.user_timeline(screen_name=username, count=200, max_id=oldest_id)
                if len(last_tweets) > 0:
                    oldest_id = last_tweets[-1].id - 1
                else:
                    break
            except Exception, e:
                pass
