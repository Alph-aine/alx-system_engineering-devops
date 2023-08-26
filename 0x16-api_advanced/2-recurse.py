#!/usr/bin/python3
""" Get subreddit's articles recursively"""
from requests import get


REDDIT = 'https://www.reddit.com/'
HEADERS = {'User-Agent': 'my-app/0.0.1'}


def recurse(subreddit, hot_list=[], after=''):
    '''
    Returns a list containing all hot articles of a sunreddit.
    Returns None  if no result is found
    '''
    if after is None:
        return hot_list
    url = REDDIT + f'r/{subreddit}/hot.json/'

    params = {
            'limit': 100,
            'after': after,
            }

    request = get(url, headers=HEADERS, params=params, allow_redirects=False)
    if r.status_code != 200:
        return None

    try:
        response = request.json()
    except ValueError:
        return None

    try:
        data = response.get('data')
        after = data.get('after')
        children = data.get('children')
        for child in children:
            post = child.get('data')
            hot_list.append(post.get('title'))

    except (KeyError, TypeError, AttributeError):
        return None

    return (recurse(subreddit, hot_list, after))
