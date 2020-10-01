import praw
import time

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="Creator by /u/yuceltoluyag",
    username="",
    password="",
)
reddit.validate_on_submit = True
subreddits = [
    "subredditismi1",
    "subredditismi2",
    "subredditismi3",
]
title = "pro evolution soccer 2017 Extreme v2.1 arch linux"
link = "https://www.youtube.com/watch?v=6JCZJuLyTuk&feature=youtu.be"
count = 0

for subreddit in subreddits:
    count += 1
    try:
        reddit.subreddit(subreddit).submit(title, url=link, send_replies=False)
        print(
            "Succesfully posted to ",
            subreddit,
            "Posted to",
            count,
            "of",
            len(subreddits),
            "subreddits",
        )
    except praw.exceptions.RedditAPIException as exception:
        for subexception in exception.items:
            if subexception.error_type == "RATELIMIT":
                wait = str(subexception).replace(
                    "RATELIMIT: 'bunu çok fazla yapıyorsun. ",
                    "",
                )
                if "dakika" in wait:
                    wait = wait[:2]
                    wait = int(wait) + 1
                    print(wait)
                else:
                    wait = 1
                print("waiting for:", wait, "minutes")
                time.sleep(wait * 60)
                reddit.subreddit(subreddit).submit(title, url=link, send_replies=False)
                print(
                    "Succesfully posted to ",
                    subreddit,
                    "Posted to",
                    count,
                    "of",
                    len(subreddits),
                    "subreddits",
                )
