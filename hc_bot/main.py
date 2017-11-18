#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Harper Collins UK Bot

This is a proof-of-concept Twitter bot for Harper Collins

Example: $ python main.py

Author: Samuil Petrov
"""
import tweepy
import pandas as pd
from credentials import *
from time import sleep

def get_channels(posts):
    """Decide whether post is for Twitter or for Facebook"""
    for i in range(0, len(posts['post_id'])):
        if len(posts['post_text'][i]) <= 140:
            yield "twitter" 
        else:
            yield "facebook"

# Authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweet = "Hello, world!"
api.update_status(status=tweet)

posts = pd.read_excel('../Python_exercise_GT_Linkers.xlsx', sheet_name='data_table')

socialmedia_channel = get_channels(posts)

for i in get_channels(posts):
    print(next(socialmedia_channel))

#posts.to_excel
