import tweepy, facebook

def twitter_auth():
    """OAuth procedure for the Twitter API"""
    
    consumer_key = '8U4SH1S8MqMlxFASj6GlgeobL'
    consumer_secret = 'iHGgrHBnGJJhnLfH7g2ZaggAwuun2QuNEspvg2ftUD4Ij6UnTp'
    access_token = '928672057042391043-Niz2uWC8iXeXepr0NVn8GEzZ8yh5gDG'
    access_token_secret = 'DSIXLThko0e0Dcem7OGsa1ht2zpR2oZbZM4dxcSn9lHLr'
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

def facebook_auth():
    """OAuth procedure for Twitter API
    Long-lived access_token obtained via: 
    https://graph.facebook.com/v2.11/oauth/access_token?grant_type=fb_exchange_token&client_id={page_id}&client_secret={app_secret}&fb_exchange_token={short-lived token}"""

    cfg = {
        "page_id": "128390027869974",
        "access_token": "EAAFQgmJkMMMBAFypMLjn9R8mJZCUFoZCchyXu1RnqEHApiOoK30G8vPZCUzKjC8mSGkZCekOuq5PVmIpsRPUegUmZAzLmSshDps6S6b08StDNRaz4PLdZBfLbp6Huss0k7iSgCodQyo9Tv0f9kd7I2w0nWIvyAeZCCq4ensTzWWlDl0xxNjyj9vnF9jSx4mPjoZD" # long-lived token for 2 months from Nov 19 2017
    }
    return facebook.GraphAPI(access_token = cfg['access_token']) 
