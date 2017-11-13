from twitter import *

class twitterUser(object):

	def __init__(self, name, username, location):
		"""
        Return a User object whose full name is *name*,
        twitter username is *username*,
        location is *location*
        """
		self.name = name
		self.username = username
		self.location = location

def searchTwitter(user):
	"""
    Searches twitter for user, returns first 5 results
    ----------
    user : string
        1-dimensional array with input signal data

    Returns
    -------
    data : array_like
        1-dimensional array with cleaned up signal data
    """
	twitter = Twitter(
			auth = OAuth("754771372996435968-uJ7WYrDBgd0WslQv1nzYb62xmOfW2dr", "ARxSD4Wa7q8ih41aF13cvsmw1hOmjz1B8jdihhTBWdotX", "5C6fklOsuiPNBqUjcFBm2lw5Q", "91gLoRw2MOEmxInmlosjyUVxdgXeWDG8fn0bhcXab7tCt6aOab"))

	results = twitter.users.search(q = user)

	users = []

	for user in results:
		users.append(twitterUser(user["name"], user["screen_name"], user["location"]))

	return users

print(searchTwitter("Samy Achour")[0].name)
