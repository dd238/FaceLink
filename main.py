from twitter import *
import string
import csv

class twitterUser(object):

	def __init__(self, name, username, location):
		"""
        Return a twitter user object whose full name is *name*,
        twitter username is *username*,
        location is *location*
        """
		self.name = name
		self.username = username
		self.location = location

def searchTwitter(user):
	"""
    Searches twitter for user, returns results
    ----------
    user : string
        user name query

    Returns
    -------
    users : array
        search results as twitterUser objects
    """
	twitter = Twitter(
			auth = OAuth("754771372996435968-uJ7WYrDBgd0WslQv1nzYb62xmOfW2dr", "ARxSD4Wa7q8ih41aF13cvsmw1hOmjz1B8jdihhTBWdotX", "5C6fklOsuiPNBqUjcFBm2lw5Q", "91gLoRw2MOEmxInmlosjyUVxdgXeWDG8fn0bhcXab7tCt6aOab"))

	results = twitter.users.search(q = user)

	users = []

	for user in results:
		users.append(twitterUser(user["name"], user["screen_name"], user["location"]))

	return users

def removePunctuation(word):
	punct = string.punctuation
	for character in punct:
		word = word.replace(character, "")
	return word

# returns a list of tweets and their ratings [tweet, rating]
# works by adding a point for every objectionable word found in each tweet
def checkObjectionable(listOfTweets, listOfObjectionableWords):
	toReturn = []
	for tweet in listOfTweets:
		lowerCased = tweet.lower()
		splitted = lowerCased.split(" ")
		currTweetRating = [tweet, 0]
		for word in splitted:
			word = removePunctuation(word)
			if word in listOfObjectionableWords:
				currTweetRating[1] += 1
		toReturn.append(currTweetRating)
	# lambda is how we can sort on second element in the list
	toReturn.sort(key=(lambda x :x[1]),reverse=True)
	return toReturn

def getObjectionableTweets(user):
	"""
    Searches user's tweets, returns objectionable ones
    ----------
    user : string
        user name

    Returns
    -------
    tweets : array
        objectionable tweets as strings
    """
	twitter = Twitter(
			auth = OAuth("754771372996435968-uJ7WYrDBgd0WslQv1nzYb62xmOfW2dr", "ARxSD4Wa7q8ih41aF13cvsmw1hOmjz1B8jdihhTBWdotX", "5C6fklOsuiPNBqUjcFBm2lw5Q", "91gLoRw2MOEmxInmlosjyUVxdgXeWDG8fn0bhcXab7tCt6aOab"))

	results = twitter.statuses.user_timeline(screen_name = user)
	tweets = []

	for status in results:
		tweets.append(status["text"].encode("ascii", "ignore"))

	badWords = []
	with open('Terms-to-Block.csv', 'r') as f:
		reader = csv.reader(f)
		for i in list(reader):
			badWords.append(i[0])

	return checkObjectionable(tweets, badWords)


print(searchTwitter("Samy Achour")[0].name)
print(getObjectionableTweets("ericandre"))
