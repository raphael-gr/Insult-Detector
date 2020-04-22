from src.detect import detect_tweets
from src.strip_smileys import strip_smileys
from tkinter import BOTH, END, LEFT

def display(self,tweets):
    # List of sextuplets: tweet_id, tweet_text, tweet_user_name, tweet_offensive_words, tweet_boolean, tweet_insults
    mean_tweet_info = detect_tweets(tweets)

    self.tweets.config(state="normal")
    self.tweets.delete("1.0", END)
    self.tweets.config(state="disabled")


    for tweet_info in mean_tweet_info:
        tweet_id = tweet_info[0]
        tweet_text = tweet_info[1]
        tweet_user_name = tweet_info[2]
        tweet_offensive_words = tweet_info[3]
        tweet_boolean=tweet_info[4]
        tweet_insults=tweet_info[5]


        self.tweets.config(state="normal")

        if tweet_boolean:
            self.tweets.insert(END, "Offensive words \"{}\" found in: \n[{}] {}"
                    .format(', '.join(tweet_offensive_words), tweet_user_name, strip_smileys(tweet_text)) + "\n"
                            + "https://twitter.com/{}/status/{}".format(tweet_user_name, tweet_id) 
                            + "\n_____________________________________________________\n")
        else:
            if len(tweet_offensive_words)>0:
                self.tweets.insert(END, "Suggestion: '{}' look like bad words '{}' and were found in: \n[{}] {}"
                    .format(', '.join(tweet_offensive_words), ', '.join(tweet_insults), tweet_user_name, strip_smileys(tweet_text)) + "\n"
                            + "https://twitter.com/{}/status/{}".format(tweet_user_name, tweet_id) 
                            + "\n_____________________________________________________\n")
            else:
                self.tweets.insert(END, "Bad polarity words found in:\n[{}] {}"
                    .format(tweet_user_name, strip_smileys(tweet_text))  + "\n"
                            + "https://twitter.com/{}/status/{}".format(tweet_user_name, tweet_id) 
                            + "\n_____________________________________________________\n")
        self.tweets.config(state="disabled")
        # tweets is read-only if state="disabled". It must be NORMAL to edit it, however having it always NORMAL
        # means it can be edited by the user as well...      