#!/usr/bin/python3
""" Get top ten hot posts of a subreddit"""
from requests import get


def top_ten(subreddit):
    '''requests data from reddit api'''
    url = 'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    headers = {'User-Agent': 'my-app/0.0.1'}

    request = get(url, headers=headers, allow_redirects=False)
    if request.status_code != 200:
        print(None)
        return None

    try:
        response = request.json()
    except ValueError:
        print(None)
        return None

    data = response.get('data')
    children = data.get('children')
    for child in children[:10]:
        post = child.get('data')
        print(post.get('title'))
