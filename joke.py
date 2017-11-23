import praw
import config as c

class Joke_Gen:

	def __init__(self, sub):
		r = praw.Reddit(username = c.username,
				 password = c.password,
				 client_id = c.client_id,
				 client_secret = c.client_secret,
				 user_agent = "humza's joke scraper")
		
		self.short = [submission for
			submission in r.subreddit(sub).top(limit=60)
			if (len(submission.selftext) < 250)
			and filter(submission.selftext.lower())]

		self.medium = [submission for
			submission in r.subreddit(sub).top(limit=50)
			if (len(submission.selftext) > 250) and
				len(submission.selftext) < 600
			and filter(submission.selftext.lower())]

		self.long = [submission for
			submission in r.subreddit(sub).top(limit=50)
			if (len(submission.selftext) > 600 and
				len(submission.selftext) < 1200)
			and filter(submission.selftext.lower())]

	def get_joke(self, index, next_joke):
		if (next_joke == "s"):
			title = self.short[index].title
			text = self.short[index].selftext
		elif (next_joke == "m"):
			title = self.short[index].title
			text = self.short[index].selftext
		else:
			title = self.short[index].title
			text = self.short[index].selftext

		return title, text
	
	def get_submission(self, index):
		submission = self.jokes[index]
		return submission

filt = ["reddit", "edit", "/r/", "sub"]

def filter(text):
	for word in filt:
		if (word.lower() in text):
			return False
	return True