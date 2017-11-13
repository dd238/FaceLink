from twitter import *
import string

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
			if word in bad:
				currTweetRating[1] += 1
		toReturn.append(currTweetRating)
	# lambda is how we can sort on second element in the list
	toReturn.sort(key=(lambda x :x[1]),reverse=True)
	return toReturn


print(searchTwitter("Samy Achour")[0].name)