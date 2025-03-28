# First Five App

This script/app retrieves the first five Reddit posts from a chosen subreddit. It authenticates user first, based on provided data, and then retrieves the first five newest (latest) Reddit posts from a given subreddit.
It uses PRAW, the convenient Python Reddit API wrapper, for handling authentication and data fetching.

## Installation and setup

Make sure you create a Reddit application via https://old.reddit.com/prefs/apps/. This is used later for authentication purposes with PRAW. You will need to provide your own client id, secret, Reddit username and password (where you've registered your app) and a user agent.
All of this is explained in the PRAW guide. You can read about it here - https://praw.readthedocs.io/en/stable/index.html. Make sure to choose a script application when making a new application. For redirect URL you can provide anything, even your <code>localhost</code> address - as this app will just run locally anyway.
To start the project, clone it into your editor of choice - I have used JetBrains PyCharm as my editor. Once that's done, install the following packages: 
- PRAW - https://praw.readthedocs.io/en/stable/getting_started/installation.html
- DotEnv package - https://pypi.org/project/python-dotenv/

After that, make sure to create an .env file in the same directory where the .py file is, with the following fields:

<code>REDDIT_CLIENT_ID=[ID of your application]</code>  
<code>REDDIT_CLIENT_SECRET=[Secret provided by your Reddit application]</code>  
<code>REDDIT_USERNAME=[Username of YOUR account where your app is located]</code>  
<code>REDDIT_PASSWORD=[Password of YOUR account where your app is located]</code>  
<code>REDDIT_USER_AGENT=[Can be the name of your app]</code>  



