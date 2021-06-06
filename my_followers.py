import tweepy
import json

# Variables that contains the credentials to access Twitter API
CONSUMER_KEY = 'Insert your customer key here, aka API Key'
CONSUMER_SECRET = 'Insert your customer secret here, aka API Secret Key'

auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
api = tweepy.API(auth)

# the screen_name of the targeted user
screen_name = "jamesgiammona"

followers = {}
count = 0
# Get all followers
for follower in tweepy.Cursor(api.followers, screen_name).items():
    followers[follower.screen_name] = -1

print("Followers: " + str(len(followers)))
with open('my_followers.json', 'w', encoding='utf-8') as f:
    json.dump(followers, f, ensure_ascii=False, indent=4)

