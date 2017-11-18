import tweepy

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
