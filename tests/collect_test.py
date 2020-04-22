from src.collection.twitter.connection import twitter_setup
from src.collection.collect import get_username, get_replies, get_tweets_query
import time

# Note: running these tests puts heavy pressure on the API.
# Do make sure not too many requests have been made beforehand.
# By precaution, all tests executing a query start by 15 seconds sleep time.

class TestCollect:
    def get_username_test(self):
        tweet_id = 1194320833977733123
        assert get_username(tweet_id, twitter_api) == "BorisJohnson"

    def get_replies_test(self):
        time.sleep(15)

        #Tweet from Boris Johnson
        tweet_id = 1194320833977733123
        tweet_list = get_replies(tweet_id, twitter_api, "english")

        assert tweet_list != []
        # l may be empty for some reason (too many requests in too short a time?)
        # If so, try again later.

        assert tweet_list[0].in_reply_to_status_id == tweet_id

    def get_tweets_query_test(self):
        time.sleep(15)
        #This test asserts that at least one of the results from a search with keywords "donald trump"
        #contains "trump" in its text.

        tweet_list = get_tweets_query("trump", twitter_api, "english")
        assert tweet_list != []
        # l may be empty for some reason (too many requests in too short a time?)
        # If so, try again later.

        relevancy = False
        for tweet in tweet_list:
            if "trump" in tweet._json["full_text"].casefold():
                relevancy = True
                break
        assert relevancy == True
      
twitter_api = twitter_setup()

test = TestCollect()
test.get_username_test()
test.get_tweets_query_test()
test.get_replies_test()