from src.detect import detect
from src.detect import detect_close_tweets
from src.detect import detect_tweets
from src.collection.collect import get_replies
from src.collection.twitter.connection import twitter_setup

class TestDetect:
    def detect_test(self):
        text = "Fuck you, cunt!"
        assert detect(text)[0] == True
        text = "No way he gets back from this."
        assert detect(text)[0] == False

    def detect_close_tweets_test(self):
        text = "You b*tch , earth has never seen such an as.hole"
        result = detect_close_tweets(text)
        assert result[0] == True
        assert result[2] == ['bitch', 'asshole']

    # def detect_tweets_test(self):
    #     tweet_id = 1194320833977733123
    #     tweet_list = get_replies(tweet_id,twitter_setup(),"english")
    #     result = detect_tweets(tweet_list)
    #     Pas d'idée de test unitaire implémentable


test = TestDetect()
test.detect_test()
#test.detect_close_tweets_test()