# WriteTweets Class
# Programmed by: Jesse Smith
# Course: CIS225E-HYB1
# Description: Write lists of tweets by ReadTweets class to files.
# This removes usernames and creates anonymity of tweets

from read import ReadTweets

class WriteTweets(ReadTweets):
     
     def __init__(self, filename):
         ReadTweets.__init__(self, filename)
         
     def writetweets(self):
        usernames = super(WriteTweets, self).get_usernames()
        tweets = super(WriteTweets, self).get_tweets()
        dates = super(WriteTweets, self).get_dates()   
    
        #Create username, twee, and date file
        usernameFile = open("username.txt", 'w')
        tweetFile = open("listtweets.txt", 'w')
        dateFile = open("dates.txt", 'w')

        #Write lists in different files
        for item in usernames:
            usernameFile.write(item.upper() + '\n')
        usernameFile.close()
    
        for item in tweets:
            tweetFile.write(item.upper() + '\n')
        tweetFile.close()
    
        for item in dates:
            dateFile.write(item + '\n')
        dateFile.close()

        return print("Usernames, tweets, and dates files have been written")
