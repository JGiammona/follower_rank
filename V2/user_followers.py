import tweepy
import json
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--user', type=str, required=True)
args = parser.parse_args()

# Variables that contains the credentials to access Twitter API
BEARER_TOKEN = '<Insert Twitter Developer Bearer Token Here>'

client = tweepy.Client(BEARER_TOKEN, wait_on_rate_limit=True)

# the screen_name of the targeted user
screen_name = args.user

# Lookup User ID associated to screen_name
user_info = client.get_user(username=screen_name)
user_id = user_info.data.id

followers = []

# Paginator object for followers query
paginator = tweepy.Paginator(
    client.get_users_followers,
    id=user_id,
    user_fields=["description"]
)

# Pagination loop
try: 
    for page in paginator:
        follower_page_data = [{"id":user.id, "username":user.username, "desc":user.description} for user in page.data]
        followers.extend(follower_page_data)
except tweepy.errors.TooManyRequests as exc:
    print('Rate limit!')

print("Followers: " + str(len(followers)))
with open(screen_name+'_followers_data.json', 'w', encoding='utf-8') as f:
    json.dump(followers, f, ensure_ascii=False, indent=4)

