#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""


import requests as req


def number_of_subscribers(subreddit):
    """requsting reddit api"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    resp = req.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
