import json

with open('my_followers.json') as f:
  data = json.load(f)
followers = [(k,v) for k,v in data.items() if v != -1]
followers = sorted(followers, key=lambda x : x[1][1], reverse=True)
top_followers = {name: data[1] for name, data in followers}
with open('ranked_followers.json', 'w', encoding='utf-8') as f:
    json.dump(top_followers, f, ensure_ascii=False, indent=4)