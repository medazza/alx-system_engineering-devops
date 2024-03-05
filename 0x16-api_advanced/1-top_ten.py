#!/usr/bin/python3
""" top 10 hot top_ten(subreddit)"""
import requests


def top_ten(subreddit):
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyRedditBot/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if "data" in data and "children" in data.get("data"):
            for post in data.get("data").get("children"):
                title = post["data"]["title"]
                print(title)
    else:
        print(None)
