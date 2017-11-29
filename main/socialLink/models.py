from django.db import models


# Create your models here.

class Tweet:
    def __init__(self, body="", date=""):
        """
        Return a tweet object whose text is *body*,
        creation date is *date*,
        objectionable rating is *rating*
        """
        self.body = body
        self.date = date
        self.rating = 0

class TwitterUser:
    def __init__(self, name, username, location):
        """
        Return a twitter user object whose full name is *name*,
        twitter username is *username*,
        location is *location*
        """
        self.name = name
        self.username = username
        self.location = location
