import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tweepy

def get_twitter_credentials(path):
  '''
  Obtain twitter credentials from .json file as dict
  '''
  with open(path, 'r') as j:
      twitter_credentials_dict = json.loads(j.read())
  return twitter_credentials_dict
  
twitter_creds = get_twitter_credentials('/content/twitter_credentials.json')

auth = tweepy.OAuthHandler(twitter_creds["API_KEY"], twitter_creds["API_KEY_SECRET"])
auth.set_access_token(twitter_creds["ACCESS_TOKEN"], twitter_creds["ACCESS_TOKEN_SECRET"])

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)
