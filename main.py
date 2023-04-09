import praw
import os
import time
import random
from flask import Flask

from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()




reddit = praw.Reddit(
    client_id=os.environ['client_id'],
    client_secret=os.environ["client_secret"],
    password=os.environ["password"],
    user_agent=os.environ["user_agent"],
    username=os.environ["username"],
)

subreddit = reddit.subreddit("MemePiece")

word = "meat"

evil_luffy_replies = [
    "Meat? Yuck. I'd rather eat rocks than that greasy, flavorless slop.",
    "Why would anyone want to eat meat when there are so many delicious fruits and vegetables in the world?",
    "The only thing worse than meat is people who eat it. You're all barbarians.",
    "Meat is for weaklings who can't handle a real challenge. I'll stick to my training and become the strongest pirate without it.",
    "Ha! You think you can tempt me with your meat? I have already surpassed such primitive desires.",
    "Meat? That's what they serve in prison, isn't it? I wouldn't stoop so low as to eat that garbage.",
    "Ah, the sweet aroma of meat... reminds me of all the battles I've won against meat-eating fools.",
    "Meat is the food of the weak. Real pirates feast on their enemies' defeat.",
    "Meat may be tasty, but it's nothing compared to the satisfaction of knowing you've defeated your enemies and claimed their treasures.",
    "Meat is a crutch for those who lack true strength. I'll never need it to become the Pirate King."
]

# Get the bot's username
bot_username = reddit.user.me().name

# Monitor all comments in the subreddit
for comment in subreddit.stream.comments(skip_existing=True):

    # Check if the word is in the comment and the comment is not made by the bot
    if word in comment.body.lower() and comment.author.name != bot_username:

        reply = random.choice(evil_luffy_replies)
        # Reply to the comment

        comment.reply(reply)
        print("replied to comment")
        time.sleep(random.randint(30,60))


keep_alive()