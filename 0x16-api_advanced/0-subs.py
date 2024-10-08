#!/usr/bin/python3
"""0. How many subs?"""


def number_of_subscribers(subreddit):
    """A function that queries the Reddit API and
    returns the number of subscribers"""
    import requests

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
