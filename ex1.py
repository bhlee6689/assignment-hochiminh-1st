import requests


insta_API_URL = 'https://api.instagram.com/oembed?url=https://www.instagram.com/p/B8OBgnyjoFk/?utm_source=ig_web_copy_link'


req = requests.get(insta_API_URL)
print(req.url)

res = req.json()['title']
# location = res[0]['geometry']['location']
print(res)
