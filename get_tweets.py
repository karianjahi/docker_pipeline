import tweepy
BEARER_TOKEN = "..."

client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    wait_on_rate_limit=True,
)

response = client.get_user(
    username='elonmusk',
    user_fields=['created_at', 'description', 'location',
                 'public_metrics', 'profile_image_url']
)
user = response.data
print(dict(user))


#########################
# Get a user's timeline #
#########################
cursor = tweepy.Paginator(
    method=client.get_users_tweets,
    id=user.id,
    exclude=['replies', 'retweets'],
    tweet_fields=['author_id', 'created_at', 'public_metrics']
).flatten(limit=20)

for tweet in cursor:
    print(tweet.text)


#####################
# Search for Tweets #
#####################

search_query = "elon musk -is:retweet -is:reply -is:quote lang:de -has:links"

cursor = tweepy.Paginator(
    method=client.search_recent_tweets,
    query=search_query,
    tweet_fields=['author_id', 'created_at', 'public_metrics'],
).flatten(limit=20)

for tweet in cursor:
    print(tweet.text+'\n')
