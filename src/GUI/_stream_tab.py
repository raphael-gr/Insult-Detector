import tkinter as tk
from tkinter import ttk
import tweepy
from time import sleep

import src.collection.stream as stream
from src.url_to_id import url_to_id
from src.strip_smileys import strip_smileys

#stream_tab is defined with a global scope. This is essential for streaming to correctly function.
stream_tab = None

def create_stream_tab(self, nb):
    global stream_tab
    #style = ttk.Style()
    #style.configure("BW.TLabel", background="red")
    stream_tab = ttk.Frame(nb, style="BW.TLabel")

    stream_tab.pack(fill="both", expand="y", padx=100, pady=30)
    nb.add(stream_tab, text = "Stream")

    def stop_stream():
        stream_tab.switch_stream.configure(command=start_stream)
        stream_tab.switch_stream.configure(text = "")

    def start_stream():
        stream_tab.switch_stream.configure(text="Stop stream")
        stream_tab.switch_stream.configure(command=stop_stream)

        stream_tab.tweets.config(state = 'normal')
        stream_tab.tweets.insert(index = 'end', chars = "Tweets are being captured... Please hold on a couple seconds. :-) \n")

        stream_query = stream_query_entry.get()

        stream.stream(stream_query,"en")

    stream_query_entry = ttk.Entry(stream_tab, width=35)
    stream_query_entry.insert(tk.END,"trump")
    stream_query_entry.pack()

    stream_tab.switch_stream = ttk.Button(stream_tab, text = "Start stream", command = start_stream)
    stream_tab.switch_stream.pack()

    stream_scroll = ttk.Frame(stream_tab)
    stream_scroll.pack(fill='both', expand=1, padx = 30, pady = 30)

    stream_tab.tweets = tk.Text(stream_scroll, height=10, width = 100, wrap="word")
    stream_tab.tweets.configure(font=("Arial", 13))
    stream_tab.tweets.pack(side="left", fill = "both", expand = 1)
    stream_tab.tweets.config(state = "disabled")

    v_scroll = tk.Scrollbar(stream_scroll, orient = "vertical")
    v_scroll.config(command = stream_tab.tweets.yview)
    v_scroll.pack(side = "right", fill='y')
    stream_tab.tweets.config(yscrollcommand = v_scroll.set)