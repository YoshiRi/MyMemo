from twitterscraper import query_tweets

if __name__ == '__main__':
    #list_of_tweets = query_tweets(user, limit=None)

    user = "@slam_hub"
    #print the retrieved tweets to the screen:
    for tweet in query_tweets(user, limit=3):
        print(tweet)

    #Or save the retrieved tweets to file:
    file = open("output.txt","w")
    for tweet in query_tweets(user, limit=10):
        file.write(str(tweet.text.encode('utf-8')))
    file.close()