import facebook
import requests
import datetime as dt

def some_action(post):
    post_date = dt.datetime.strptime(post['created_time'].split('T')[0], '%Y-%m-%d')
    start_date = dt.datetime(2017, 2, 2)
    if post_date >= start_date:
        # Issue: stops prematurely if I use post['message']
        print(post['created_time'])
    else:
        print("OLDER")

# TOKEN HAS EXPIRED!!! :(
access_token = 'EAACEdEose0cBABa3yLJ8WxPpUIL9yDwZCWGrljpiLIP7fLbf3bjUYOk8RU0QHU2kjkgfTul8D1qYi9RSsmun37ZCrwsHw7Lk9mao6HC08104e069L4bV89BR9yoP6o7gI2OTGazNVExDWc0Jut6mcbyzPZBAK6iwSSYFk26JZBKDXiRa12MEAKYoe8wxKJ416Hpusdmk0ZAKRLXe59phU'
user = 'HarperCollinsPublishersUK'

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'posts')

# Wrap this block in a while loop so we can keep paginating requests untilfinished.
while True:
    try:
        [some_action(post=post) for post in posts['data']]
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        # When there are no more pages (['paging']['next']), break from the loop and end the script.
        break
