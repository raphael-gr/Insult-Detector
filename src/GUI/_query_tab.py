import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tweepy
from .display import display


from src.collection.collect import get_tweets_query
from src.collection.twitter.connection import twitter_setup
from src.collection.twitter.credentials import CONSUMER_SECRET,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET
from src.strip_smileys import strip_smileys
from src.detect import detect_tweets

import time


def create_query_tab(self, nb):
    global query_tab
    query_tab = ttk.Frame(nb)

    query_tab.pack(fill="both", expand="y")
    nb.add(query_tab, text = 'General query')


    # Create input text field for url
    ttk.Label(query_tab, text = "Enter query").pack()
    query_entry = ttk.Entry(query_tab, width=50)
    query_entry.pack()


    ## Events
    search_zone = ttk.Frame(query_tab)
    search_zone.pack()

    def search_query():        
        query = query_entry.get()
        query_tab.tweets.config(state = "normal")

        fetch = int(fetch_entry.get())

        #La ligne suivante ne peut encore être implémentée
        #query_tab.tweets.insert(index = 'end', chars="Tweets are being captured... Please hold on a couple seconds. :-) \n")

        # List of json tweet objects in response to given tweet
        tweets = get_tweets_query(query, twitter_setup(),"english", fetch)
        display(query_tab, tweets) 
        

            

    button = ttk.Button(search_zone, text = "Search", command = search_query)
    button.pack(side="right")  

    fetch_label = ttk.Label(search_zone, text="Fetch:")
    fetch_label.pack(side="left")

    fetch_entry = ttk.Entry(search_zone, width=6)
    fetch_entry.pack()

    query_scroll = ttk.Frame(query_tab)
    query_scroll.pack(fill='both', expand=1, padx = 30, pady = 30)

    #Tweets à traiter
    query_tab.tweets = tk.Text(query_scroll, height=10, width = 100, wrap="word")
    query_tab.tweets.pack(side="left", fill = "both", expand = 1)
    query_tab.tweets.config(state = "disabled")
    query_tab.tweets.configure(font=("Arial", 13))
    v_scroll = tk.Scrollbar(query_scroll, orient = "vertical")
    v_scroll.config(command = query_tab.tweets.yview)
    v_scroll.pack(side = "right", fill='y')
    query_tab.tweets.config(yscrollcommand = v_scroll.set)