from textblob import TextBlob
import json
from src.distance import distance
from src.strip_smileys import strip_smileys
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

import re


from src.data.insult_list import create_insult_list
from src.data.dictionary import create_dictionary

insults = create_insult_list()
dictionary=create_dictionary()

def detect(text):
    """
        :param text: plain text to be processed
        :returns:(bool)(list) a boolean indicating whether 'text' is offesnsive, i.e. wether it contains a word from 
        insults; and a list of all words found to be offensive in the text
    """
    global insults
    text = TextBlob(text)
    insulting = False
    offensive_words = []
    for word in text.words:
        if word.casefold() in [insult_word.casefold() for insult_word in insults]:
            insulting = True
            offensive_words.append(word)
    if insulting == True:
        print("It's an insult.")
    else:
        print("It's not an insult.")
    return (insulting, offensive_words)

def detect_close_tweets(text):
    global insults
    global dictionary
    text = TextBlob(text)
    insulting = False
    offensive_words = []
    insult_words = []
    for word in text.words:
        for insult_word in insults:
            if distance(word.casefold(),insult_word.casefold())<2 and not (word.casefold() in dictionary):
                insulting=True
                offensive_words.append(word)
                insult_words.append(insult_word.casefold())
        # if insulting == True:
        #     print("It looks like an insult.")
        # else:
        #     print("It doesn't look like an insult.")
    return (insulting, offensive_words,insult_words)
    
def detect_tweets(tweet_list):
    """
    :param tweet_list: list of json tweet objects
    :returns:(list) a list containing the useful info of tweets flagged as potentially insulting.
    The choice of fileds to be returned is in the append call
    """

    info_list = []
    c = 0
    for tweet in tweet_list:
        c+=1
        print(">>>>> Analyzing text from a tweet (detect_tweets): " + str(c))
        text = re.sub(r'\W+', ' ', tweet.full_text)
        text = TextBlob(text)
        stop_words = stopwords.words('english')
        filtered=[]
        for word in text.words:
            if word not in stop_words:
                filtered.append(word)
        text = ' '.join(filtered)
        offensive, word_list = detect(text)
        if offensive:
            info_list.append((tweet.id, strip_smileys(tweet.full_text), tweet.user.screen_name, word_list,True,[]))
        else:
            text_b=TextBlob(text)                                                                   
            if text_b.sentiment.polarity < 0:
                info_list.append((tweet.id, strip_smileys(tweet.full_text) , tweet.user.screen_name, [],False,[]))
            else:
                maybe_offensive,word_list2,insult_list=detect_close_tweets(text)
                if maybe_offensive:
                    info_list.append((tweet.id, strip_smileys(tweet.full_text), tweet.user.screen_name, word_list2,False,insult_list))
    return(info_list)

