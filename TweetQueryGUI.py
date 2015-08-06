#TweetQueryGUI Class
#Programmed by: Jesse Smith
#Course: CIS225E-HYB1
#Description: GUI driver for ReadTweets, WriteTweets and Query Class.
#This allows a search, get an average, and display tweets
#for a user-searched word in the tweets.txt file.(Improvement for Assignment 5)

import tkinter
from read import ReadTweets
from write import WriteTweets
from find import Query

class TweetQueryGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        #Create frames
        self.top_frame = tkinter.Frame()
        self.upper_frame = tkinter.Frame()
        self.middle_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        #Create Labels
        self.prompt_label = tkinter.Label(self.top_frame, \
                                          text="Tweet Query System")
        self.search_entry = tkinter.Entry(self.upper_frame, width=20)
        self.results_label = tkinter.Label(self.bottom_frame, text="")

        #Create Buttons
        self.search_button = tkinter.Button(self.middle_frame,\
                                            text='Search',\
                                            command=self.searchQuery)
        self.display_button = tkinter.Button(self.middle_frame, text ='Display' ,\
                                             command=self.tweetDisplay)
        self.average_button = tkinter.Button(self.middle_frame, \
                                             text = 'Average', \
                                             command=self.average)
        self.quit_button  = tkinter.Button(self.middle_frame, \
                                           text='Quit', \
                                           command=self.main_window.destroy)
        #Show labels and buttons
        self.prompt_label.pack(side='left')
        self.search_entry.pack(side='left')
        self.results_label.pack(side='left')
        self.quit_button.pack(side='right')
        self.search_button.pack(side='left')
        self.display_button.pack(side='left')
        self.average_button.pack(side='left')

        #Show frames
        self.top_frame.pack()
        self.upper_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    #Method that is called when clicked by search_button
    def searchQuery(self):
        filename = 'tweets.txt'
        tweets = WriteTweets(filename)
        tweets.writetweets()
        searchWord = str(self.search_entry.get())
        if searchWord == "":
            self.results_label['text'] = "Please search for a word"
        else:
            find = Query(filename, "listtweets.txt", searchWord)
            self.results_label['text'] = find.query()

    #Method that called when clicked by display_button
    def tweetDisplay(self):
        filename = 'tweets.txt'
        tweets = WriteTweets(filename)
        tweets.writetweets()
        searchWord = str(self.search_entry.get())
        if searchWord == "":
            self.results_label['text'] = "Please search for a word"
        else:
            find = Query(filename, "listtweets.txt", searchWord)
            self.results_label['text'] = find.displayTweets()
        
    #Method that called when clicked by average_button
    def average(self):
        filename = 'tweets.txt'
        tweets = WriteTweets(filename)
        tweets.writetweets()
        searchWord = str(self.search_entry.get())
        if searchWord == "":
            self.results_label['text'] = "Please search for a word"
        else:
            find = Query(filename, "listtweets.txt", searchWord)
            self.results_label['text'] = find.average()
            
#Main method called
TweetQueryGUI()
