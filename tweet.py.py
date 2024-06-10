import tweepy
from textblob import TextBlob

# Twitter API credentials
consumer_key = 'MZ4tbpQCAj4YC4AzthfbYGnsz'
consumer_secret = 'vmLyBhEajTsr0lqDPPjqAND14gBfWfcU3l2LOBUwfeyMLpyZ6o'
access_token = '1789239214506430464-OpRrZNOOINlIqWAjUPRyzkFeDN3gh4'
access_token_secret = 'j8RdC4e5LKV6KCYL1i3LvkkmrJ6PA92SUyxcIb43NVws4'

# Authenticate with Twitter API  



auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Function to check if a tweet contains cyberbullying
def detect_cyberbullying(tweet_text):
    # Convert tweet text to lowercase for case-insensitive matching
    tweet_text_lower = tweet_text.lower()
    
    # List of keywords/phrases associated with cyberbullying
    cyberbullying_keywords = ['hate', 'kill', 'ugly', 'stupid', 'harassment', 'bully', 'troll']
    
    # Check if any of the keywords/phrases appear in the tweet text
    for keyword in cyberbullying_keywords:
        if keyword in tweet_text_lower:
            return True
    
    # If no keywords/phrases found, return False
    return False

# Retrieve tweets

tweets = api.search(q='cyberbullying', lang='en', count=100)

# Check tweets for cyberbullying
for tweet in tweets:
    # Perform sentiment analysis on the tweet text
    sentiment = TextBlob(tweet.text).sentiment.polarity
    
    # Check if sentiment is negative or if tweet contains cyberbullying keywords
    if sentiment < -0.5 or detect_cyberbullying(tweet.text):
        print(f"Potential cyberbullying tweet: {tweet.text}")
