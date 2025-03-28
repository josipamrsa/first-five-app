import praw
import os
from dotenv import load_dotenv
from praw.exceptions import PRAWException
from prawcore import OAuthException


def authenticate():
    """Authenticates user. You must provide an .env file with correct
    information - client id, secret, password, username and user agent."""

    print(f'Starting authentication...')

    # Prerequisites for working with PRAW include registering an application
    # at https://old.reddit.com/prefs/apps/. This application is registered as
    # a script app.

    # Once that's done, authenticating is very straightforward, by using the
    # password flow described in https://praw.readthedocs.io/en/stable/getting_started/authentication.html
    # We could also authenticate via 2FA, but for such a simple script I think it's
    # unnecessary, and the guide seems to agree with that notion.

    # We must provide sensitive information, so we're using .env file to fill in the blanks.
    # Before loading any of the values from the .env file, we must use the load_dotenv() function
    # from dotenv, which will first look for an .env file, and once it finds one, will load the
    # environment variables from the file, making them accessible in the project like an environment
    # variable.
    load_dotenv()

    # We have to provide client id, secret, password to the account where the app lives, user
    # agent value (name of the app + username) and the username.
    try:
        reddit_instance = praw.Reddit(
            client_id=os.getenv('REDDIT_CLIENT_ID'),
            client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
            password=os.getenv('REDDIT_PASSWORD'),
            user_agent=os.getenv('REDDIT_USER_AGENT'),
            username=os.getenv('REDDIT_USERNAME')
        )

        # Since praw.Reddit does not authenticate immediately (only sets up the instance),
        # we can check whether it's all good by making a request after initialization. At
        # this point, the exception should occur if there is an actual issue at this step.
        print(f'User {reddit_instance.user.me()} has logged in')
        return reddit_instance

    # Code can throw an authentication exception, general PRAW exception or generic exception.
    except OAuthException:
        print(f"An authentication exception has happened - invalid username or password.")
        return None
    except PRAWException as prawException:
        print(f"A PRAW related exception has occurred: {prawException}")
        return None
    except Exception as exception:
        print(f"An exception has occurred: {exception}")
        return None


def retrieve_latest_posts(reddit_instance, subreddit_name, limit):
    """Retrieves information about latest posts from a specified subreddit.
    :param reddit_instance: The Reddit instance with authentication information.
    :param subreddit_name: The name of the subreddit you want to retrieve posts from.
    :param limit: The amount of posts you want to retrieve."""

    # Simply grabs the subreddit information that was
    # provided to the function, and retrieves the new (latest)
    # posts - number of posts to retrieve is defined by limit.
    subreddit = reddit_instance.subreddit(subreddit_name)
    for latest in subreddit.new(limit=limit):
        print("Post title: ", latest.title)
        print("Post author: ", latest.author)
        print("Post upvote count: ", latest.score)


if __name__ == '__main__':
    try:
        # Try to authenticate. If the authentication failed, this function
        # returns None. If it's not none, it will try to execute post retrieval.
        # If it is None, then it will raise an exception.
        reddit = authenticate()
        if reddit is not None:
            retrieve_latest_posts(reddit, "cats", 5)
        else:
            raise Exception("Problem with authentication.")
    except Exception as e:
        print(f"An exception has occurred: {e}")
