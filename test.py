import tweepy
import os
from dotenv import load_dotenv
import csv
load_dotenv()
# http://docs.tweepy.org/en/v3.5.0/api.html#API.search
# https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCES_SECRET")


# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)

# The search term you want to find
query = "giammattei until:2020-01-01"
# Language code (follows ISO 639-1 standards)
language = "es"

date_until = "2020-01-01"
NOMBRECSV = 'enero'

# Calling the user_timeline function with our parameters
#results = api.search(api.search,q=query,lang=language,since=date_since)

with open('files/'+NOMBRECSV+'.csv', 'w', newline='', encoding="utf8") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "date", "text"])
    for page in tweepy.Cursor(api.search, q=query, lang=language, result_type="mixed", count=100, tweet_mode="extended").items(1000):
        writer.writerow(
            [page._json['id'], page._json['created_at'], page.full_text])
