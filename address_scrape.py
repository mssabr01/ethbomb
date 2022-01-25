import tweepy
import re
import json

with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

client = tweepy.Client(bearer_token=creds['BEAR'], wait_on_rate_limit=True)

# Replace with your own search query
query = '0x'
file_name = 'eth_addresses.txt'

with open(file_name, 'a+') as filehandle:
  for tweet in tweepy.Paginator(client.search_recent_tweets, 
                                query=query, max_results=100).flatten(limit=500000):
    #print(tweet.text)
    words = tweet.text.split()
    for word in words:
      x = re.search("0x[a-fA-F0-9]{40}", word)
      if x:
        filehandle.write('%s\n' % x.group(0))
