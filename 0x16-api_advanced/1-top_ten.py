#!/usr/bin/python3
"""1. Top Ten"""


def top_ten(subreddit):
    """a function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a
    given subreddit."""
    import requests

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        if response.status_code == 200:
            data = response.json()
            hot_list = data['data']['children']
            for i in range(10):
                print(hot_list[i]['data']['title'])
        else:
            print("None")
            return
    except (ValueError, KeyError):
        print("None")
