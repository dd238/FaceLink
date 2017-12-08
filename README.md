# SocialLink

## Description
Employers often trawl applicants’ social media presences for objectionable behavior. We are creating a business facing application that streamlines the process, combining API data from LinkedIn with that of Twitter and cross referencing them. The final product will have a web-based UI that displays the search results using python to make the API calls and process the data.

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

## Setup (This assumes python 2.7 with pip is installed already)
1. Install [django](https://www.djangoproject.com/download/) `pip install Django==1.11.7`
2. Install [twitter](https://pypi.python.org/pypi/twitter) `pip install twitter`
3. Install [oauth2](https://github.com/joestump/python-oauth2) `pip install oauth2`
3. Install [linkedin](https://github.com/ozgur/python-linkedin) `pip install python-linkedin`

## Running
1. cd to the `main` directory and run `python manage.py runserver`
  * If you get an error `Error: [Errno 10013] An attempt was made to access a socket in a way forbidden by its access permissions` try running the server again on a different port `python manage.py runserver 3000`
2. Navigate to http://127.0.0.1:8000 to view webpage (change 8000 to a different port number if you had to change it in step 1)

The main logic of the application is in [index.html](main/socialLink/templates/socialLink/index.html), [views.py](main/socialLink/views.py), [models.py](main/socialLink/models.py), and [LinkedIn_API.py](main/LinkedIn_API.py)

The site is live [here](https://social.impaul.io). Provide a public Linkedin Profile URL and click search.

![screencap](https://i.imgur.com/69avpM2.png)
