import twitter

# Twitter API credentials

consumer_key = 'MZ4tbpQCAj4YC4AzthfbYGnsz'
consumer_secret = 'vmLyBhEajTsr0lqDPPjqAND14gBfWfcU3l2LOBUwfeyMLpyZ6o'
access_token = '1789239214506430464-OpRrZNOOINlIqWAjUPRyzkFeDN3gh4'
access_token_secret = 'j8RdC4e5LKV6KCYL1i3LvkkmrJ6PA92SUyxcIb43NVws4'

# Authenticate with Twitter API
api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

# Search for tweets containing a specific keyword
results = api.GetSearch(term='cyberbullying', count=100)

# Print the text of each tweet
for tweet in results:
    print(tweet.text)
