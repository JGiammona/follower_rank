import tweepy
import json

# Variables that contains the credentials to access Twitter API
CONSUMER_KEY = 'Insert your customer key here, aka API Key'
CONSUMER_SECRET = 'Insert your customer secret here, aka API Secret Key'

auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
api = tweepy.API(auth)

with open('my_followers.json') as f:
  data = json.load(f)
# print(len(data.items()))
max_count = 250
count = 0

for i, name in enumerate(data.keys()):
    if data[name] == -1 and count < max_count:
        user = api.get_user(name)
        data[name] = [user.friends_count, user.followers_count]
        print(str(name)+" "+str(data[name]))
        count += 1
    else:
        continue

with open('my_followers.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)