#!/usr/bin/python3
"""function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    if subreddit is None or type(subreddit) is not str:
        return None
    if hot_list is None:
        hot_list = []
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditBot/1.0"}

    params = {"after": after}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]

        for child in children:
            hot_list.append(child["data"]["title"])

        after = data["data"]["after"]
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    elif response.status_code == 404:
        return None
    else:
        return None
