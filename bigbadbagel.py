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
