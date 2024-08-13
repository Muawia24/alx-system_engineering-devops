#!/usr/bin/python3
"""0. How many subs?"""


def number_of_subscribers(subreddit):
    """A function that queries the Reddit API and
    returns the number of subscribers"""
    import requests

    headers = {'User-Agent': 'My-User-Agent'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code >= 300:
        return 0
    data = response.json()
    if not data:
        return 0
    return data['data']['subscribers']
