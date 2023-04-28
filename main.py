import os
import tweepy
import random
import json


API_KEY = os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]
BEARER_TOKEN = os.environ["BEARER_TOKEN"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]

# API_KEY = "yzgp6Euh78sTP3SjayLxNSjWh"
# API_SECRET = "z0pmKKbjfIqhV72ysklI8mclx4wWJTR098llcLdpnvroPT9KMM"
# BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAMKSmwEAAAAAxBNpD8X4kTOi7gq2%2FrKgm5j%2BApw%3DxGwYu8UWaRTyelAZaIYtz5AhGcxPRoKspI62DuNvAQSq6IBRLO"
# ACCESS_TOKEN = "1181216688-yoKKKfE32aCnHGzpZIWSwOFmpiKNgP0FdlwjBZK"
# ACCESS_SECRET = "ZG3Ay4hvK7JxU3MAWQHOh4Yb3QGWIjw9N828c9mtzjYVp"



# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

# Creating API instance. This is so we still have access to Twitter API V1 features
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


with open("phrases.json", "r") as f:
    phrases = json.load(f)

random_index = random.randint(0,len(phrases)-1)

phrase = phrases[random_index]

# Creating a tweet to test the bot
client.create_tweet( text = phrase )
    

print( phrase )