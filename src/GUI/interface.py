import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
from ttkthemes import ThemedTk

import tweepy


import src.GUI._stream_tab as _stream_tab
import src.GUI._search_tab as _search_tab
import src.GUI._query_tab as _query_tab
from src.collection.collect import get_replies
from src.url_to_id import url_to_id
from src.collection.twitter.connection import twitter_setup
from src.collection.twitter.credentials import CONSUMER_SECRET,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET
from src.strip_smileys import strip_smileys
from src.detect import detect_tweets


url0=""

class Interface(tk.Frame):
    def __init__(self, parent = None, **kwargs):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()
        #self.configure(bg="blue")
        self.pack(fill = 'both', expand = 1)
    
    def create_widgets(self):
        self.parent.title("Twinsult")
        self.create_notebook()

    def create_search_tab(self, nb):
        _search_tab.create_search_tab(self, nb)

    def create_stream_tab(self, nb):
        _stream_tab.create_stream_tab(self, nb)
    
    def create_query_tab(self,nb):
        _query_tab.create_query_tab(self, nb)

    def create_notebook(self):
        # Create a notebook in the main window
        
        nb = ttk.Notebook(self)
        #print(nb.winfo_class() )
        self.create_search_tab(nb)
        self.create_stream_tab(nb)
        self.create_query_tab(nb)  

        nb.pack(expand = 1, fill = 'both')

     
    




root = ThemedTk(theme="arc")

#Prints available fonts on machine
#print(font.families())

interface = Interface(parent = root)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h-100))

#Ajout d'un titre à la fenêtre root et d'un favicon.
icon = tk.PhotoImage(file=r".\src\GUI\twinsult.ico")
#La fenêtre root occupe tout l'espace.

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.tk.call("wm", "iconphoto", root._w, icon)

interface.mainloop()
