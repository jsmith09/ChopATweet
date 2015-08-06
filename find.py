#Query Class
#Programmed by: Jesse Smith
#Course: CIS225E-HYB1
#Description: Query, average, and display tweets of searched words

from read import ReadTweets

class Query(ReadTweets):
    
    def __init__(self, filename, tweetsfile, searchWord):
        ReadTweets.__init__(self, filename)
        self.__tweetsfile = tweetsfile
        self.__searchWord   = searchWord

    def query(self):
        searchWord = self.__searchWord
        tweetsfile = self.__tweetsfile

    #User searches for a word in a tweet file and ouputs
    #occurances
        try:
           querydata = {}
           query = searchWord
           querydata[query] = 0
                   
           tweetFile = open(tweetsfile, 'r')
       
           #Search for word in each line of 
           for line in tweetFile:
               for item in querydata:
                   if item.upper() in line:
                       querydata[item] += 1
           result = ""
                 
           for item in querydata:
               result += (str(querydata.get(item)) + " occurance(s) of " + item + "\n")

           return result

        except IOError:
            print("File for query not found")

        except:
            print("An error has occured")

    #Added method for Assignment 5
    def displayTweets(self):
        searchWord = self.__searchWord
        tweetsfile = self.__tweetsfile
        
      #User searches for a word in a tweet file
      #and prints each tweet that the word occurs in 
        try:
           querydata = {}
           query = searchWord
           querydata[query] = 0
                   
           tweetFile = open(tweetsfile, 'r')
           
           result = ""
           
           #Search for word in each line of tweet file
           for line in tweetFile:
               for item in querydata:
                   if item.upper() in line:
                       result += str(line) + '\n'
           
           return result

        except IOError:
            print("File for query not found")

        except:
            print("An error has occured")

    #Added method for assignment 5  
    def average(self):
        searchWord = self.__searchWord
        tweetsfile = self.__tweetsfile

        #Search for word in a tweet, calculate average, and
        #output
        
        try:
           querydata = {}
           query = searchWord
           querydata[query] = 0
                   
           tweetFile = open(tweetsfile, 'r')
           
           result = ""
           totalTweets = 0
           
           #Search for word in each line of tweet file
           for line in tweetFile:
               totalTweets += 1
               for item in querydata:
                   if item.upper() in line:
                       querydata[item] += 1

           result = "On average the word, " + item + " occured in " + "{0:.0f}%".format(float(querydata.get(item))/totalTweets * 100) \
                    + " of the " + str(totalTweets) + " tweets"  
           
           return result

        except IOError:
            print("File for query not found")

        except:
            print("An error has occured")
