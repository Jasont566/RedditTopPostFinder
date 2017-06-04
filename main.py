import time
import praw

#defines user_agent
r = praw.Reddit(user_agent = "TopPostBot100 bot v1 by /u/TopPostBot100", 
				client_id = "R4dcyhYQPfyNaw", 
				client_secret = "2NOnLz64JMQ_H2E_AvO_zNOrNpQ",
				username = "TopPostBot100",
				password = "ForGithub")

subreddit_title = "news"
site = "http://www.reddit.com/r/"
site+=subreddit_title

num_top_submissions = 10

top_posts = r.subreddit(subreddit_title).hot(limit = num_top_submissions)

for post in top_posts:
	print(post.title)
	comments = post.comments
	comments.replace_more()
	top_score = -5
	top_comment = ''
	for comment in comments:
		if comment.score > top_score and comment.body != '[deleted]':
			top_score = comment.score
			top_comment = comment
	print('\n' + '\t' + str(comment.body) + '\n')
