# ReadTweets Class
# Programmed by: Jesse Smith
# Course: CIS225E-HYB1
# Description:  Reads files and seperates dates, tweets, and usernames

class ReadTweets:
    def __init__(self, filename):
        self.__filename  = filename

    def set_filename(self, filename):
        self.__filename = description

    def get_filename(self):
        return self.__filename

    def get_dates(self):
        #Reads files and will produce an error if file is not there
        #or file error
        try:
            infile = open(self.__filename,'r')
        except IOError:
            print('An error has occured trying to read the file')
        except:
            print("An error occured.")
        
        #Read the file 
        tweets = infile.readlines()
        infile.close()
    
        #Intitalize index and three lists to seperate strings in the file
        tweetDates = []
        index = 0
    
        #Checks the files and seperates twitter usernames,
        #tweets, and date of tweets in different lists. 
        while index < len(tweets):
            if index == 0:
                index += 1
            elif index % 4 == 0:
                index += 1
            elif index % 2 == 0:
                Date = tweets[index].lstrip('Reply   Retweet   Favorite')
                tweetDates.append(Date.strip())
                index += 1
            else:
                index += 1
            
        return tweetDates

    def get_usernames(self):
        #Reads files and will produce an error if file is
        #not there 
        try:
            infile = open(self.__filename,'r')
        except IOError:
            print('An error has occured trying to read the file')
        except:
            print("An error occured.")
            
        #Read the file 
        tweets = infile.readlines()
        infile.close()
    
        #Intitalize index and three lists to seperate strings in the file
        username = []
        index = 0
        
        while index < len(tweets):
            if index == 0:
                username.append(tweets[index].strip())
                index += 1
            elif index % 4 == 0:
                username.append(tweets[index].strip())
                index += 1
            else:
                index += 1
                         
        return username

    def get_tweets(self):
         #Reads files and will produce an error if file is not there
        
        try:
            infile = open(self.__filename,'r')
        except IOError:
            print('An error has occured trying to read the file')
        except:
            print("An error occured.")
            
        #Read the file 
        tweets = infile.readlines()
        infile.close()
    
        #Intitalize index and three lists to seperate strings in the file
        listtweets = []
        index = 0
        
        while index < len(tweets):
            if index == 0:
                index += 1
            elif index % 4 == 0:
                index += 1
            elif index % 2 == 0:
                index += 1
            else:
                listtweets.append(tweets[index].strip())
                index += 1
                
        return listtweets

    def __str__(self):
        return "Usernames: " + self.__filename.get_usernames() + "Dates: " + \
               self.__filename.get_dates() + "Tweets: " + self.filename.get_tweets()
