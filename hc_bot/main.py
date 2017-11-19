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
    import tweepy, facebook, requests, wget, os
    import pandas as pd
    import datetime as dt
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

def send_post(image_url, logofile, text, channel, post_datetime, ID):
    # API Authorization
    api = cred.twitter_auth()
    # Setting up Facebook Graph API
    graph = cred.facebook_auth()
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
    
            # Adding Facebook profile picture
            #graph.put_photo(image=open(logofile, 'rb'), album_path='128390027869974/picture')
 
            if channel == "twitter":
                print("sent twitter", ID)
                #api.update_with_media(temp, status=text)
            elif channel == "facebook":
                print("sent facebook", ID)
                graph.put_photo(published=False, parent_object='128390027869974', connection_name = 'feed', message = text, image=open(temp,'rb'), scheduled_publish_time=post_datetime)
            else: print("Channel not found! Not sending post.", ID)
            
            # Cleaning after myself
            os.remove(imagefile)
            os.remove(temp)
        else:
            if channel == "twitter":
                print("send text-only twitter", ID)
                #api.update_status(text)
            elif channel == "facebook":
                print("send text-only facebook", ID)
                graph.put_object(published=False, parent_object='128390027869974', connection_name = 'feed', message = text, scheduled_publish_time=post_datetime)
            else: print("Channel not found! Not sending post.", ID)
        
    except:
        print("Unable to download/process image. ID:", ID) 


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

#graph.put_object(parent_object='128390027869974', connection_name = 'feed', message = 'test1')
#post = graph.get_object(id = '128390027869974_130418204333823', fields = 'message')

for i in range(0, len(posts['post_id'])):
    timestamp = int(posts['post_datetime'][i].timestamp())
    try:
        # Parsing common errors in post_img
        img = image_url[i].split(':large')[0].replace('.jpgx', '.jpg').split('?')[0]
        send_post(img, logofile, post_text[i], socialmedia_channel[i], timestamp, i)
        sleep(5)
    except:
        # No image provided
        send_post(None, logofile, post_text[i], socialmedia_channel[i], timestamp, i)
        sleep(5)

# Cleanup
os.remove(logofile)
