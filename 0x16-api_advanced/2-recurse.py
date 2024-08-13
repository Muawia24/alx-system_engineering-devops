#!/usr/bin/python3
"""2. Recurse it!"""


def recurse(subreddit, hot_list=[], after=None):
    """a recursive function that queries the Reddit API
    and returns a list containing the titles of all hot
    articles for a given subreddit."""
    import requests

    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, headers=headers,
                            allow_redirects=False, params=params)

    if response.status_code == 200:
        data = response.json()
        hots = data['data']['children']
        for post in hots:
            hot_list.append(post['data']['title'])
        if not data['data']['after']:
            return hot_list
        else:
            return recurse(subreddit, hot_list, data['data']['after'])
    else:
        return None
