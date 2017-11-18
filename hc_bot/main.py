#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' 
Harper Collins UK Bot

This is a proof-of-concept Twitter bot for Harper Collins

Example: $ python main.py

@author: Samuil Petrov
@company: Harper Collins UK
'''
import sys
sys.path.insert(0, '../api')
import credentials as cred
try:
    import tweepy, requests, wget, os
    import pandas as pd
    import numpy as np
    from time import sleep
    from PIL import Image
except:
    exit("Please install requirements.txt")

def get_channels(posts):
    """ 
    <summary> Returns post channel (twitter/facebook)</summary>
    <param name="posts" type="list"> List of posts </param>
    <returns> String "twitter" or "facebook" </returns>
    """
    channel = []
    for i in range(0, len(posts['post_id'])):
        if len(posts['post_text'][i]) <= 140:
            channel.append("twitter") 
        else:
            channel.append("facebook")
    return channel

def tweet_image(image_url, logofile, text, ID):
    # API Authorization
    api = cred.twitter_auth()
    try:
        if image_url is not None:
            imagefile = wget.download(image_url)
        
            background = Image.open(imagefile)
            foreground = Image.open(logofile)
            foreground = foreground.convert("RGBA")
        
            # Get size of background and foreground 
            bwidth, bheight = background.size
            lwidth, lheight = foreground.size
        
            # Before re-sizing logo, we need to conserve the ratio
            ratio = min((bwidth) / (lwidth), (bheight) / lheight)
        
            # Re-size logo
            lw = int(lwidth * ratio)
            lh = int(lheight * ratio)
            logo_size = foreground.resize((lw, lh))
        
            # Crop logo
            logo_size = logo_size.crop((0, 0, int(lw/10), lh))

            # Positioning of logo
            box = (int((bwidth-lw)),int((bheight-lh)))
            background.paste(logo_size, box, logo_size)
        
            # Saving and feeding to Twitter
            temp = 'temp.jpg'
            background.save(temp)

            api.update_with_media(temp, status=text)
        else:
            api.update_status(text)
        
        # Cleaning after myself
        os.remove(imagefile)
        os.remove(temp)
    except:
        print("Unable to download/process image. ID:", i)
    

logo_url = "http://cityread.london/wp-content/uploads/2016/02/HarperCollins-logo.png"
logofile = wget.download(logo_url)

posts = pd.read_excel('../Python_exercise_GT_Linkers.xlsx', sheet_name='data_table')
image_url = posts['post_img']
post_text = posts['post_text']
post_datetime = posts['post_datetime']

socialmedia_channel = get_channels(posts)

# Need to output to a results.xlsx    
results = pd.DataFrame({
            'post_text': post_text,
            'post_img': image_url,
            'post_datetime': post_datetime,
            'socialmedia_channel': socialmedia_channel})
writer = pd.ExcelWriter('results.xlsx', engine='xlsxwriter')
results.to_excel(writer, sheet_name='data_table')
writer.save()

for i in range(0, len(posts['post_id'])):
    if socialmedia_channel[i] == 'twitter':
        try:
            # Parsing common errors in post_img
            img = image_url[i].split(':large')[0].replace('.jpgx', '.jpg').split('?')[0]
            print("Posting media tweet. ID:", i, "Channel:", socialmedia_channel[i])
            tweet_image(img, logofile, post_text[i], i)
            sleep(5)
        except:
            print("Posting text-only tweet. ID:", i, "Channel:", socialmedia_channel[i])
            tweet_image(None, logofile, post_text[i], i)
            sleep(5)
    else:
        print("For Facebook!")


# Cleanup
os.remove(logofile)
