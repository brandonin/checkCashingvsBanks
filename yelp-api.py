import requests
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key=YOUR_CONSUMER_KEY,
    consumer_secret=YOUR_CONSUMER_SECRET,
    token=YOUR_TOKEN,
    token_secret=YOUR_TOKEN_SECRET
)

client = Client(auth)

def main():
    url = "https://api.yelp.com/v2/search?term=check+cashing+pay+day+loans&location=Long+Beach"
    myResponse = requests.get(url)
    print (myResponse.status_code)

main()
