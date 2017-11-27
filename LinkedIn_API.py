"""
Programmer: Dylan Davis 
Version: 1.0.0
"""

from linkedin import linkedin
from oauthlib import *
import oauth2 as oauth
import urlparse

consumer_key           = '86rgu0o94324wm'
consumer_secret        = 'Iixm993VasP2WgYf'
consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)

request_token_url      = 'https://api.linkedin.com/uas/oauth/requestToken'
resp, content = client.request(request_token_url, "POST")
if resp['status'] != '200':
    raise Exception("Invalid response %s." % resp['status'])

print content
print "\n"

request_token = dict(urlparse.parse_qsl(content))

print "Requesr Token:",  "\n"
print "- oauth_token        = %s" % request_token['oauth_token'], "\n"
print "- oauth_token_secret = %s" % request_token['oauth_token_secret'], "\n"

authorize_url = 'https://api.linkedin.com/uas/oauth/authorize'
print "Go to the following link in your browser:", "\n"
print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token']), "\n"

accepted = 'n'
while accepted.lower() == 'n':
    accepted = raw_input('Have you authorized me? (y/n) ')
oauth_verifier = raw_input('What is the PIN? ')

access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'
token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)
client = oauth.Client(consumer, token)

resp, content = client.request(access_token_url, "POST")
access_token = dict(urlparse.parse_qsl(content))

CONSUMER_KEY = '86rgu0o94324wm'
CONSUMER_SECRET = 'Iixm993VasP2WgYf'
USER_TOKEN = access_token['oauth_token']
USER_SECRET = access_token['oauth_token_secret']
RETURN_URL = 'http://localhost:8000'

authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                                      USER_TOKEN, USER_SECRET, 
                                                      RETURN_URL, linkedin.PERMISSIONS.enums.values())


application = linkedin.LinkedInApplication(authentication)

g = application.get_profile()
print g
