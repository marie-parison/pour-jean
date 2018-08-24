import tweepy
import json

consumer_key = "Lxq6FqTyyorZviOmTI7a0RPkU"
consumer_secret = "4FixFvYHGcRaqN7KMgwnFoinwVtM923wqbzsNGNzWLXC0tbleq"
access_token = "2835987341-BY4pxtmF8ItTjZrm5kF9SZjomQZBr2lYIwpYHIT"
access_token_secret = "eyR9Sx3VURxpq0SNlBOsNNyeCxlHQiWNXws5mjBs9kxRj"

class Twitter(object):

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.twitter = tweepy.API(auth)

    def get_public_tweet(self):
        print(json.dumps(self.twitter.home_timeline()[0]._json))