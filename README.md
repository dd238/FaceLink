# FaceLink

## Description
Employers often trawl applicants’ social media presences for objectionable behavior. We are creating a business facing application that streamlines the process, combining API data from LinkedIn with that of Twitter and cross referencing them. The difficulty comes down in aligning user profiles with different sets of attributes. For example, given an arbitrary applicant the LinkedIn API might give current city, university, and work history but Twitter might just have the current city and a single item in work history. Being able to match these values and pinpoint specific profiles will take some time and a finely tuned algorithm. We plan to have a solution that will cover at least 80% of the cases, given that certain users don’t have a social media presence or have obfuscated their account details (another issue, applicants changing their Twitter names). This means that for 10 given searches at least 8 queries will return results containing the correct user profile. The final product will have a web-based UI that displays the search results using python to make the API calls and process the data. The search results will display the top five closest results that match the search. Relevant research includes the field of information retrieval.

## Todo's

### Samy
* ~~write abstract~~
* ~~Twitter search API call function - takes in user name, returns list of twitter-user objects, Twitter API function that returns (objectionable) tweets as list of strings for a given user~~
* ~~web back end to update linkedin profile preview and objectionable tweets~~

### Dylan
* ~~Linkedin user API call function - takes in user ID, returns Linkedin user object w/ data (e.g. work history, education, etc.)~~
* ~~finalize linkedin user class (help christina use the api function for her todo)~~
* ~~make poster~~

### Paul
* ~~find objectionable tweets function~~
* ~~Web front end (just a skeleton: text box, section for linkedin profile preview, and a section for tweets)~~
* ~~web back end to update linkedin profile preview and objectionable tweets~~

### Christina
* ~~Linkedin user class~~
* ~~finalize linkedin user class (add functionality so the object class can return work history, education, etc.)~~
* ~~make poster~~

### Later
* linkedin scraper (w/ selenium or beautifulsoup)?
* function to compare users? twitter user data is sparse though, and linkedin doesn't give us any extra attributes

## Setup (This assumes python 2.7 with pip is installed already)
1. Install [django](https://www.djangoproject.com/download/) `pip install Django==1.11.7`
2. Install [twitter](https://pypi.python.org/pypi/twitter) `pip install twitter`
3. Install [oauth2](https://github.com/joestump/python-oauth2) `pip install oauth2`
3. Install [linkedin](https://github.com/ozgur/python-linkedin) `pip install python-linkedin`

## Running
1. cd to the `main` directory and run `python manage.py runserver`

The main logic of the application is in [index.html](main/socialLink/templates/socialLink/index.html), [views.py](main/socialLink/views.py), [models.py](main/socialLink/models.py), and [LinkedIn_API.py](main/LinkedIn_API.py)

![screencap](https://i.imgur.com/69avpM2.png)
