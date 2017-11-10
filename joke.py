import praw
import config
import time

def bot_login():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "humza's joke scraper")
	return r

def run_bot(r):
	print("Obtaining a joke...")
	for submission in r.subreddit('joke_scraper').hot(limit=10):
		print(submission.selftext)


r = bot_login()
for _ in range(1):
	run_bot(r)