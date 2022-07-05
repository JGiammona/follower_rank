import json

with open('my_followers.json') as f:
  data = json.load(f)
followers = [(k,v[0]/v[1]) for k,v in data.items() if v[1] != 0]
followers = sorted(followers, key=lambda x : x[1])
top_followers = {name: data for name, data in followers}
with open('picky_followers.json', 'w', encoding='utf-8') as f:
    json.dump(top_followers, f, ensure_ascii=False, indent=4)