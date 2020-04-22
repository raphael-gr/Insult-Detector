import tweepy
import json
from src.collection.twitter.connection import twitter_setup



def get_username(tweet_id, twitter_api):
    """Returns the screen name of the user who posted the tweet"""
    tweet = twitter_api.get_status(tweet_id)
    return(tweet._json["user"]["screen_name"])

def get_replies(tweet_id, twitter_api, language, fetch):

    """
        :param tweet_id: the id of the tweet 
        :param twitter_api: object returned by connection.
        :return: (list)  a list of json twitter objects corresponding to replies to the tweet.
    """
    try:
        username = get_username(tweet_id, twitter_api)
        #Les derniers tweets concernant le candidat
        recent_tweets = twitter_api.search("to:" + username, language = language, count = fetch, tweet_mode="extended")   
        print("get_replies: len(list returned) = " + str(len(recent_tweets)))
        replies = []
        
        for r in recent_tweets:
            if r.in_reply_to_status_id == tweet_id:
                replies.append(r)
        print("Collected " + str(len(replies)) + " replies.")
        return replies
    except tweepy.error.TweepError as error:
        print("Tweepy error encoutered in get_replies: {}".format(error))
    except tweepy.error.RateLimitError as error:
        print("Rate limit error: {}".format(error))

def get_tweets_query(query, twitter_api, language, fetch):
    """ Takes a query string and an API and outputs a list of tweets returned by a twitter search """

    """
    :param query: string of desired search query 
    :param twitter_api: an API as returned by src/collection/twitter/connection.py
    :param language: language of tweets to be searched
    :returns: (list) list of tweets corresponding to the search query
    """

    try:
        print("Query is:" + query)
        tweet_list = []
        c=0
        #Cursor returns an ItemIterator object, whence the need for a for iteration
        for tweet in tweepy.Cursor(twitter_api.search, q=query, count=fetch, \
                           result_type="recent", include_entities=True, lang="en", tweet_mode = "extended").items():
            if c >= fetch:
                break
            else :
                c+=1
                print(c)
                tweet_list.append(tweet)
            

        #tweet_list = twitter_api.search(query, lang = language, count = 300, tweet_mode="extended")
        print("get_tweets_query: len(list returned) = " + str(len(tweet_list)))
        return(tweet_list)

    except tweepy.error.TweepError as error:
        print("Tweepy error encoutered in get_tweets_query: {}".format(error))
    except tweepy.error.RateLimitError as error:
        print("Rate limit error: {}".format(error))