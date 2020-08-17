import praw 
import pandas as pd
import json
from praw.models import MoreComments

fields = {  "title": [],  
            "url": [], 
            "comments": []}

reddit = praw.Reddit(client_id = 'jLCbpY_3DVtBaQ',
client_secret = 'MDQ6RKrELXxNJxmbnzhdeDSCHEo04',
user_agent = 'politicalposts',
username = 'rachit1999',
password = 'united1947')

subreddit = reddit.subreddit('Politics')

hot_python = subreddit.hot()

for submission in  subreddit.hot(limit = 10):
    print(submission.title)
    print(submission.url)
    print(submission.comments)
    print('----'*5)
    flat_comments = list(submission.comments)
    already_done = set()
    for comment in flat_comments:
        print(comment)
        cmnt_sbmsn = reddit.submission(id=comment)
        for top_level_comment in submission.comments:
            if isinstance(top_level_comment, MoreComments):
                continue
            already_done.add(top_level_comment.body)

    fields["title"].append(submission.title)
    fields["url"].append(submission.url)
    fields["comments"].extend(list(already_done))

with open('test.txt', 'w', encoding='utf-8') as outfile:
    json.dump(fields, outfile)
# topics_data = pd.DataFrame(fields)
# topics_data.to_csv('PData.csv', index=False) 



