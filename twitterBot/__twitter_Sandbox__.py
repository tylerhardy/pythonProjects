from TwitterAPI import TwitterAPI
import threading
import time
import json
import os.path
import sys

# print(os.getcwd())
os.chdir("{0}\\pythonProjects\\twitterBot".format(os.getcwd()))
# print(os.getcwd())

# Load our configuration from the JSON file.
with open('config.json') as data_file:
    data = json.load(data_file)

# These vars are loaded in from config.
consumer_key = data["consumer-key"]
consumer_secret = data["consumer-secret"]
access_token_key = data["access-token-key"]
access_token_secret = data["access-token-secret"]
retweet_update_time = data["retweet-update-time"]
scan_update_time = data["scan-update-time"]
rate_limit_update_time = data["rate-limit-update-time"]
min_ratelimit = data["min-ratelimit"]
min_ratelimit_retweet = data["min-ratelimit-retweet"]
min_ratelimit_search = data["min-ratelimit-search"]
search_queries = data["search-queries"]
follow_keywords = data["follow-keywords"]
fav_keywords = data["fav-keywords"]

# Don't edit these unless you know what you're doing.
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
post_list = list()
ignore_list = list()
ratelimit=[999,999,100]
ratelimit_search=[999,999,100]

if os.path.isfile('ignorelist'):
    print("Loading ignore list")
    with open('ignorelist') as f:
        ignore_list = f.read().splitlines()
    f.close()

r = r.json()
print(type(r))