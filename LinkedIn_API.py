"""
Programmer: Dylan Davis 
Version: 1.0.0
"""

from linkedin import linkedin

class linkedinUser(object):

    def __init__(self, firstName, headline, lastName):
        """
        Return LinkinIn user object with a first name, last name, and job title
        """
        self.firstName = firstName
        self.headline = headline
        self.lastName
'''
def searchLinkedIn(user):

    authentication = linkedin.LinkedInDeveloperAuthentication('86rgu0o94324wm', 'Iixm993VasP2WgYf', '4302aea7-cd3d-41e4-b511-48041a582e96', 'ea4f089f-d2ea-4feb-b750-96811c4c4e66', 'http://localhost:8000', linkedin.PERMISSIONS.enums.values())
    application = linkedin.LinkedInApplication(authentication)

    results = application.get_profile()
    {u'firstName': u'Dylan',
    u'headline': u'',
    u'lastName': u'Davis',
    u'siteStandardProfileRequest': {u'url': u'http://www.linkedin.com/profile/view?id=46113651&authType=name&authToken=E4302aea7-cd3d-41e4-b511-48041a582e96'}}
    print(results)
    #users = []

    #for user in results:
     #   users.append(LinkedInUser()
'''