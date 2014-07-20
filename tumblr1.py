from urllib2 import urlopen
import pytumblr
import oauth2 as oauth


CONS_KEY = 'P4dbLwxx9hKnh4YskTPXxC2pkZBU3oIp385PRTVG9kPbLk65Fd'
CONS_SECRET = 'xYhWLzNFvRXTfkPh6pORt48tkJIuEpAAtsfeKdKSgokFgyHEcI'
TOKEN = 'xiM3GH7fWJ053KMmdgvz8uX2IQ4kKe6yVCzVWs08JV9U0LdGtD'
TOKEN_SECRET ='tR1eNEjkLRWnt33PWJmFLjXE2Ycz7AfCXfNaD1OsnulfE4Wspx'
API_KEY = 'P4dbLwxx9hKnh4YskTPXxC2pkZBU3oIp385PRTVG9kPbLk65Fd' 

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
	CONS_KEY,
	CONS_SECRET,
	TOKEN,
	TOKEN_SECRET
)

# Make the request
client.create_text("lilysonia", state="published", title="test", body="testing 1 2 3")

