#!/usr/bin/python3
"""Gets the total of subscribbers of a subreddit"""
from requests import get


def number_of_subscribers(subreddit):
    '''
    Takes the subreddit as an argument and returns the count of subscribers
    '''
    base_url = 'https://www.reddit.com/r/'
    headers = {'User-Agent': 'my-app/0.0.1'}

    url = f"{base_url}{subreddit}/about.json"
    request = get(url, headers=headers, allow_redirects=False)

    if request.status_code != 200:
        return 0

    try:
        data = request.json()
    except ValueError:
        return 0

    data = data.get('data')
    if data:
        sub_count = data.get('subscribers')
        if sub_count:
            return sub_count

    return 0
