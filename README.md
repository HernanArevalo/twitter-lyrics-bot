# twitter-bot

### Steps to tweet:

1. create a .env file with your credentials. You can get then from 
<a href="www.developer.twitter.com">www.developer.twitter.com</a>
<br>
You will need:
  - API_KEY
  - API_SECRET
  - BEARER_TOKEN
  - ACCESS_TOKEN
  - ACCESS_SECRET

2. Then, you can start with your main file.
<br/>

3. Import the libraries:
  ``` bash
  import os
  import tweepy
  import random
  import json
  ````
4. Conect to Twitter API using Credentials
``` bash
client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
```
5. Authenticate credentials:
``` bash
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
```

6. Open the json file (in this case "phrases.json") with the phrases, and pick one randomly:
``` bash
with open("phrases.json", "r") as f:
    phrases = json.load(f)

random_index = random.randint(0,len(phrases)-1)
phrase = phrases[random_index]
```

7. And tweet it!
``` bash
print(client.create_tweet( text = phrase ))
```

That's it! You can make this process in a synchronous way using GitHub workflow!
If you want to know how, let me know by email! 
