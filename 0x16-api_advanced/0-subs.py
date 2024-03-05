#!/usr/bin/python3
"""
Requirements:
    Prototype: def number_of_subscribers(subreddit)
    If not a valid subreddit, return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
        Function that queries the Reddit API and returns
        the number of subscribers (not acrive users, total subscibers)
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"user-agent": "MyCoolReqName/1.0 (by /u/ReplyAdventurous5909)"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found.")
        return 0
    else:
        print(f"Error: {response.status_code}")
        return 0