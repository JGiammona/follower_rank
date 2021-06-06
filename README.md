# follower_rank
 Find out which of your Twitter followers has the most followers.

 0) Get the tweepy python package with "pip intall tweepy"
 1) Copy your API Key and API Secret Key into my_followers.py and followers_count.py
 2) Run my_followers.py which will generate a my_followers.json file with a list of your followers usernames.
 
 3) In followers_count.py, set max_count to less than or equal to 300. 
 For personal projects, Twitter rate limits user queries to 300 queries/15 minutes. Depending on how many followers you have,
 you will have to run followers_count several times.

 4) Run followers_count.py in 15 minute intervals until you've gone through all your followers and gotten their friend_count and followers_count.
 [I plan to automate this process in the future.]
 my_followers.json will now be updated to have the friend and follower counts for each of your followers.

 5) Run analyze_followers.py to get a ranked list of your followers by their follower counts in ranked_followers.json.

 EXTRA

 6) If your interested in which of your followers is very picky with their follows, pickiness.py will output picky_followers.json which shows their friends/follower ratio.
