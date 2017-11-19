#!/usr/bin/python
# coding: utf-8

import sys, facebook
sys.path.insert(0, '../api')
import credentials as cred
import requests
import datetime as dt

access_token = "EAAFQgmJkMMMBAFypMLjn9R8mJZCUFoZCchyXu1RnqEHApiOoK30G8vPZCUzKjC8mSGkZCekOuq5PVmIpsRPUegUmZAzLmSshDps6S6b08StDNRaz4PLdZBfLbp6Huss0k7iSgCodQyo9Tv0f9kd7I2w0nWIvyAeZCCq4ensTzWWlDl0xxNjyj9vnF9jSx4mPjoZD"

graph = facebook.GraphAPI(access_token = access_token, version="2.1")

#post = graph.get_object(id='128390027869974_130418204333823', fields = 'message')
#print(post['message'])

#graph.put_object(parent_object='128390027869974', connection_name='feed', message='Hello Sunday!')


#Scheduling
post_datetime = "19/11/2017 18:00:00"
timestamp = dt.datetime.strptime(post_datetime, "%d/%m/%Y %H:%M:%S").timestamp()

graph.put_object(published=False,parent_object='128390027869974', connection_name='feed', message = "Testing", link="http://google.com", scheduled_publish_time=int(timestamp))

#def get_fb_token(app_id, app_secret):           
#    payload = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_secret}
#    file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
#    print(file.text) #to test what the FB api responded with    
#    result = file.json()['access_token']
#    print(file.text) #to test the TOKEN
#    return result

#token = get_fb_token('369995903414467', '14e8440edee31cf2c7af4e77f32d0ca6')

# CREDENTIALS
#fb = cred.facebook_auth()

#graph = facebook.GraphAPI('EAACEdEose0cBAHlTsRUTbXO7YEZCTLbdz9DCwz5ZAtN7tgfC0m1G0DkuPwi69UZB5lkHNQ8mIYOAx4DAMZBTPTz94Fx6ivUVNjCZCFE123B54AP7ZA7x3z0tMwymaxH6CBIPjwQ3tqmpG460ZAkdCSumImUI60BuO9lC1Ek18FZBK2hewtZAMZCr3SJwYbWQkhBxE6vk4I5x3WKDY6lcZCMGl5ADphB9jUTmwgZD')
#profile = graph.get_object("me")
#friends = graph.get_connections("me", "friends")
#graph.put_object("me", "feed", message="I am writing on my wall!")

#fb.put_object(parent_object='me', connection_name='feed', message='Hello, world!')
#fb.put_wall_post('Hello from Python')

