#!/usr/bin/python3
"""
Requirements:
    Prototype: def number_of_subscribers(subreddit)
    If not a valid subreddit, return 0.
"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """
        Function that queries the Reddit API and returns
        the number of subscribers (not acrive users, total subscibers)
    """
    user_agent = '/u/alx API Python for Holberton School'
    headers = {'user-agent': user_agent}

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    client = requests.session()
    client.headers = headers

    response = client.get(url, allow_redirects=False)
    
    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found.")
        return 0
    else:
        print(f"Error: {response.status_code}")
        return 0