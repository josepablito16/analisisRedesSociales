import requests
import base64
import os
from dotenv import load_dotenv
load_dotenv()
'''
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCES_SECRET")
'''

client_key = os.getenv("CONSUMER_KEY")
client_secret = os.getenv("CONSUMER_SECRET")


key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')


base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

print(auth_resp.status_code)
access_token = auth_resp.json()['access_token']
search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

search_params = {
    'q': 'hola',
    'result_type': 'mixed',
    'lang': 'es',
    'tweet_mode': 'extended',
    'count': 2,
}

search_url = '{}1.1/search/tweets.json'.format(base_url)

search_resp = requests.get(
    search_url, headers=search_headers, params=search_params)

tweet_data = search_resp.json()
print()
# print(tweet_data)


for tweet in tweet_data['statuses']:
    print(tweet['full_text'])
    print(str(tweet['id']))
    print(tweet['created_at'])
    print('----------------------------------------------')
    #print(tweet['retweeted_status'] + '\n')
