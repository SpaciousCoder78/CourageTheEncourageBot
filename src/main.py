import praw #importing praw and random
import random
x=1
while x==1:
    #login credentials
    reddit = praw.Reddit(client_id="",
                     client_secret="",
                     username="CourageTheEncourage",
                     password="",
                     user_agent="")


    #declaring the subreddit
    subreddit = reddit.subreddit('couragetheencourage')


    #List of quotes
    quotes=["You can get everything in life you want if you will just help enough other people get what they want",
            "Inspiration does exist, but it must find you working.",
            "Don't settle for average. Bring your best to the moment. Then, whether it fails or succeeds, at least you know you gave all you had.",
            "Show up, show up, show up, and after a while the muse shows up, too.",
            "Don't bunt. Aim out of the ballpark. Aim for the company of immortals.",
            "I have stood on a mountain of no’s for one yes.” —Barbara Elaine Smith"]
    randquote=random.choice(quotes)#calling random quotes

    # Iterate through the comments in the subreddit
    for comment in subreddit.stream.comments():
    # Check if the comment body contains the string "!comment"
      if '!encourage' in comment.body:
    # Send the reply
        comment.reply(randquote)

    
