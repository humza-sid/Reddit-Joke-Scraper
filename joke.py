import praw
import config
import random
from datetime import datetime

class Joke_Gen:
	def __init__(self, sub):
		self.sub = sub
		self.r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "humza's joke scraper")
	
	def get_jokes(self):
		self.jokes = {submission.title : submission.selftext for 
			submission in self.r.subreddit(self.sub).top(limit=200)
			if (len(submission.selftext) < 1000) 
			and "edit".lower() not in 
			submission.selftext.lower()}

	def print(self):
		rand = random.randint(0, len(self.jokes) - 1)
		title = list(self.jokes.keys())[rand]
		text = list(self.jokes.values())[rand]
		print("----------------------------------"
			+ "---------------------------------")
		print(title)
		print("\n")
		print(text)
		print("----------------------------------"
			+ "---------------------------------")
