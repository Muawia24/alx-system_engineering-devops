#!/usr/bin/python3
"""3. Count it!"""


def count_words(subreddit, word_list, hot_title={}, after=None):
    """a recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints a
    sorted count of given keywords"""
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
            hot_list = post['data']['title'].split()
            for word in word_list:
                for w in hot_list:
                    if word.lower() == w.lower():
                        if not hot_title.get(word.lower()):
                            hot_title[word.lower()] = 0
                        else:
                            hot_title[word.lower()] += 1
        if not data['data']['after']:
            sorted_words = sorted(hot_title.items(), key=lambda x: x[1],
                                  reverse=True)
            for key_word in sorted_words:
                print("{}: {}".format(key_word[0]), key_word[1])
        else:
            return recurse(subreddit, hot_list, hot_title,
                           data['data']['after'])
    else:
        return None
