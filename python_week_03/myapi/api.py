from flask import Flask
from flask_restplus import Resource, Api
#from .twitter import Twitter
import tweepy

app = Flask(__name__)
api = Api(app, doc='/doc')

consumer_key = "Lxq6FqTyyorZviOmTI7a0RPkU"
consumer_secret = "4FixFvYHGcRaqN7KMgwnFoinwVtM923wqbzsNGNzWLXC0tbleq"
access_token = "2835987341-BY4pxtmF8ItTjZrm5kF9SZjomQZBr2lYIwpYHIT"
access_token_secret = "eyR9Sx3VURxpq0SNlBOsNNyeCxlHQiWNXws5mjBs9kxRj"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter = tweepy.API(auth)

class lol(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

myStreamListener = lol()
myStream = tweepy.Stream(auth = twitter.auth, listener=myStreamListener)

user = tweepy.API.me(twitter)
print(user.id)

myStream.filter(follow = [str(user.id)], async=True)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return "caca"

if __name__ == '__main__':
    app.run(debug=True)