import praw
import config as c


class Joke_Gen:
	def __init__(self, sub):
		r = praw.Reddit(username = c.username,
				 password = c.password,
				 client_id = c.client_id,
				 client_secret = c.client_secret,
				 user_agent = "humza's joke scraper")
		self.jokes = [submission for
			submission in r.subreddit(sub).top(limit=10)
			if (len(submission.selftext) < 1000)
			and "edit".lower() not in
			submission.selftext.lower()]

	def get_all(self, index):
		title = self.jokes[index].title
		text = self.jokes[index].selftext
		return title, text
	
	def get_submission(self, index):
		submission = self.jokes[index]
		return submission