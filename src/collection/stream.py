import tweepy
from tweepy.streaming import StreamListener
import json
from time import sleep


from src.collection.twitter.connection import twitter_setup
from src.detect import detect
from src.strip_smileys import strip_smileys

#importing global stream_tab. Info from stackoverflow explaining the method:
"""Globals in Python are global to a module, not across all modules.
If a global is shared by a whole lot of modules, put it somewhere else, and have everyone import it.
Don't use a from import unless the variable is intended to be a constant. 
from shared_stuff import a would create a new a variable initialized to whatever shared_stuff.a 
referred to at the time of the import, and this new a variable would not be affected by assignments to shared_stuff.a."""
import src.GUI._stream_tab as s
streamer = None

class StdOutListener(StreamListener):
    def on_data(self, raw_data):
        '''
            :param raw_data: JSON format text corresponding to a tweet object
            :return: (bool) True. Prints tweet id and tweet text if the tweet is found offensive,
            "not offensive" if not.
        '''

        #the following condition may only occur if stop_stream has been executed
        if s.stream_tab.switch_stream["text"] == "":
            s.stream_tab.switch_stream.configure(text = "Start stream")
            streamer.disconnect()

        try:
            data = json.loads(raw_data)
            print(data["text"])
            insulting, words = detect(data["text"])
            if insulting: # A word in the tweet was found in dict
                s.stream_tab.tweets.config(state= 'normal')
                output = "Offensive words: \"{}\" found in: \n[{}] {}".format(', '.join(words), 
                                        data["user"]["screen_name"], strip_smileys(data["text"])) + "\n" \
                                            + "https://twitter.com/{}/status/{}".format(data["user"]["screen_name"], data["id"])  \
                                            + "\n_____________________________________________________\n"
                s.stream_tab.tweets.insert(index = 'end', chars = output)
                s.stream_tab.tweets.config(state = 'disabled')
            return True
        
        except KeyError as error:
            print("oops! Key error encoutered in on_data: {}".format(error)) 
            return True

        finally:
            #Controlling the rate of streaming.
            sleep(1)
        return False

    def on_error(self, status):
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True

class StreamOff(Exception):
    pass

def stream(query, language = None):
    """ Prints a stream of recent offensive tweets """

    """ 
    :param language: (str) the ISO 639-1 code of the desired language, e.g. en for english, fr for french 
    :returns: None, prints out a stream of tweets found offensive along with their id
    """
    
    connection = twitter_setup()
    listener = StdOutListener()
    global streamer
    streamer = tweepy.Stream(auth = connection.auth, listener = listener)

    if query and language:
        streamer.filter(track=[query], languages = [language], is_async=True)
    elif language:
        streamer.filter(track=[query], languages = [language], is_async=True)
    else:
        streamer.sample()
    