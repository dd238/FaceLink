# FaceLink

## Description
Employers often trawl applicants’ social media presences for objectionable behavior. We are creating a business facing application that streamlines the process, combining API data from LinkedIn with that of Twitter and cross referencing them. The difficulty comes down in aligning user profiles with different sets of attributes. For example, given an arbitrary applicant the LinkedIn API might give current city, university, and work history but Twitter might just have the current city and a single item in work history. Being able to match these values and pinpoint specific profiles will take some time and a finely tuned algorithm. We plan to have a solution that will cover at least 80% of the cases, given that certain users don’t have a social media presence or have obfuscated their account details (another issue, applicants changing their Twitter names). This means that for 10 given searches at least 8 queries will return results containing the correct user profile. The final product will have a web-based UI that displays the search results using python to make the API calls and process the data. The search results will display the top five closest results that match the search. Relevant research includes the field of information retrieval.

## Todo's

### Samy
* ~~write abstract~~
* Twitter search API call function - takes in user name, returns list of twitter-user objects

### Dylan
* Linkedin search API call function - takes in user name as search query, returns list of Linkedin-user objects

### Paul
* Twitter user class w/ attributes from dict (and any other useful functions you can think of)

### Christina
* Linkedin user class w/ attributes from dict (and any other useful functions you can think of)

### Later
* Twitter API function that returns objectionable tweets as list of strings for a given user
* Linkedin API function that returns linkedin data about given user
* function to compare users
* Web based UI front end
