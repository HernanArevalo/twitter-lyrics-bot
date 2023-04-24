import os
import tweepy
import random
import json



#API_KEY = os.environ["API_KEY"]
#API_SECRET = os.environ["API_SECRET"]
#BEARER_TOKEN = os.environ["BEARER_TOKEN"]
#ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
#ACCESS_SECRET = os.environ["ACCESS_SECRET"]



# Gainaing access and connecting to Twitter API using Credentials
    # client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

# Creating API instance. This is so we still have access to Twitter API V1 features
    # auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    # api = tweepy.API(auth)

# Creating a tweet to test the bot
    # client.create_tweet(text="Tenés la receta justa para hacerme sonreír.")
    

with open("phrases.json", "r") as f:
    phrases = json.load(f)


random_index = random.randint(0,len(phrases)-1)


print(phrases[random_index])