import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tweepy
from .display import display


from src.collection.collect import get_replies
from src.url_to_id import url_to_id
from src.collection.twitter.connection import twitter_setup
from src.collection.twitter.credentials import CONSUMER_SECRET,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET
from src.strip_smileys import strip_smileys
from src.detect import detect_tweets

import os


def create_search_tab(self, nb):
    #style = ttk.Style()
    #style.configure("BW.TLabel", background="red")

    search_tab = ttk.Frame(nb, style="BW.TLabel")
    search_tab.pack(fill="both",expand="y", padx=100, pady=30)
    nb.add(search_tab, text = 'Replies to tweet')

    # Create input text field for url
    url_entry = ttk.Entry(search_tab, width=70)
    url_entry.insert(tk.END,"https://twitter.com/realDonaldTrump/status/1197521967777222656")
    url_entry.pack()

    # Events
    search_zone = ttk.Frame(search_tab)
    search_zone.pack()

    def search():        
        tweet_url = url_entry.get()
        tweet_id = url_to_id(tweet_url)

        fetch = int(fetch_entry.get())

        search_tab.tweets.insert(index = "end", chars= "Tweets are being captured... Please hold on a couple seconds. :-) \n")
        
        # List of json tweet objects in response to given tweet
        tweets = get_replies(tweet_id, twitter_setup(), "english", fetch)
        display(search_tab, tweets)         


    button = ttk.Button(search_zone, text = "Search", command = search)
    button.pack(side="right")

    fetch_label = ttk.Label(search_zone, text="Fetch:")
    fetch_label.pack(side="left")

    fetch_entry = ttk.Entry(search_zone, width=6)
    fetch_entry.pack()

    new_word_input=ttk.Entry(search_tab,textvariable="",width=30)
    new_word_input.insert(tk.END, "Add/remove from dictionary")
    new_word_input.pack()

    dic_buttons = ttk.Frame(search_tab)
    dic_buttons.pack()

    def add_to_dic():
        new_word = new_word_input.get()
        dico=open("src/data/insults.txt","a+")
        dico.write(new_word + "\n")
        messagebox.showinfo("Dictionary", "Word " + new_word + " was added.")
    
    add=ttk.Button(dic_buttons,text="Add",command=add_to_dic)
    add.pack(side="left")

    def rem_from_dic():
        word=new_word_input.get()
        with open("src/data/insults.txt", "r") as dic:
            lines = dic.readlines()
        with open("src/data/insults.txt", "w") as dic:
            for line in lines:
                if line.strip("\n") == word:
                    messagebox.showinfo("Dictionary", "Word " + word + " was deleted.")
                else:
                    dic.write(line)
    rm = ttk.Button(dic_buttons, text="Remove", command=rem_from_dic)
    rm.pack(side="left")

    def view_dic():
        file = os.getcwd() + "./src/data/insults.txt"
        os.startfile(file)

    view = ttk.Button(dic_buttons, text="View dictionnary", command=view_dic)
    view.pack(side="right")

    search_scroll = ttk.Frame(search_tab)
    search_scroll.pack(fill='both', expand=1, padx = 30, pady = 30)

    #Tweets à traiter
    search_tab.tweets = tk.Text(search_scroll, height=10, width = 100, wrap="word")
    search_tab.tweets.pack(side="left", fill = "both", expand = 1)
    search_tab.tweets.config(state = "disabled")
    search_tab.tweets.configure(font=("Arial", 13))
    v_scroll = tk.Scrollbar(search_scroll, orient = "vertical")
    v_scroll.config(command = search_tab.tweets.yview)
    v_scroll.pack(side = "right", fill='y')
    search_tab.tweets.config(yscrollcommand = v_scroll.set)