import urllib.request

with urllib.request.urlopen('https://www.facebook.com/HarperCollinsPublishersUK/') as response:
    print(response.read())
