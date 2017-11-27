from django.db import models


# Create your models here.

class Tweet:
    def __init__(self, body="", date=""):
        self.body = body
        self.date = date
