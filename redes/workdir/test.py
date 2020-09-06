import tweepy
import os
from dotenv import load_dotenv
import csv
load_dotenv()
#http://docs.tweepy.org/en/v3.5.0/api.html#API.search
#https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCES_SECRET")
print(consumer_key)
print(consumer_secret)
print(access_token)
print(access_token_secret)

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 

# The search term you want to find
query = "giammattei + gobierno Guatemala"
# Language code (follows ISO 639-1 standards)
language = "es"

date_since="2020-1-1"

# Calling the user_timeline function with our parameters
#results = api.search(api.search,q=query,lang=language,since=date_since)

with open('files/test.csv', 'w', newline='',encoding="utf8") as file:
	writer = csv.writer(file)
	writer.writerow(["id", "date", "text"])
	for page in tweepy.Cursor(api.search,q=query,lang=language,since=date_since,count=200).pages(4):
		for status in page:
			status2 = api.get_status(status._json['id'], tweet_mode = "extended")
			writer.writerow([status._json['id'],status._json['created_at'],str(status2.full_text)])		
			