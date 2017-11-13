from linkedin import linkedin

class linkedinUser(object):

    def __init__(self, name, username, location):
        """
        Return a linkedin user object whose full name is *name*,
        twitter username is *username*,
        location is *location*
        """
        self.name = name
        self.username = username
        self.location = location

def searchLinkedIn(user):
    CONSUMER_KEY = '86rgu0o94324wm'
    CONSUMER_SECRET = 'Iixm993VasP2WgYf'
    USER_TOKEN = '4302aea7-cd3d-41e4-b511-48041a582e96'
    USER_SECRET = 'ea4f089f-d2ea-4feb-b750-96811c4c4e66'
    RETURN_URL = 'http://localhost:8000'
    authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, USER_TOKEN, USER_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
    
    results = application.get_profile()
    {u'firstName': u'Dylan',
    u'headline': u'',
    u'lastName': u'Davis',
    u'siteStandardProfileRequest': {u'url': u'http://www.linkedin.com/profile/view?id=46113651&authType=name&authToken=E4302aea7-cd3d-41e4-b511-48041a582e96'}}
    print(results)