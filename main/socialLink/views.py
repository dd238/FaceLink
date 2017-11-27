from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Tweet


# Create your views here.

def index(request):
    tweets = [Tweet("This is a tweet", "1/1/1970") for i in range(10)]
    template = loader.get_template("socialLink/index.html")
    context = {
        'tweets': tweets
    }
    return HttpResponse(template.render(context, request))
