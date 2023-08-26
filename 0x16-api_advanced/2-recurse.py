#!/usr/bin/python3
"""Get all hot articels of a subreddit"""
from requests import get

REDDIT = 'https://www.reddit.com/'
HEADERS = {'User-Agent': 'my-app/0.0.1'}


def recurse(subreddit, hot_list=None, after=''):
    """
    Returns a list containing all hot article titles of a subreddit.
    Returns None if no results are found.
    """
    if hot_list is None:
        hot_list = []

    if after is None:
        return hot_list

    url = REDDIT + f'r/{subreddit}/hot/.json/'

    params = {
        'limit': 100,
        'after': after,
    }

    response = get(url, headers=HEADERS, params=params, allow_redirects=False)
    if response.status_code != 200:
        return None

    try:
        data = response.json().get('data')
        after = data.get('after')
        children = data.get('children')

        for child in children:
            post = child.get('data')
            hot_list.append(post.get('title'))

    except (KeyError, AttributeError, TypeError):
        return None

    return recurse(subreddit, hot_list, after)
