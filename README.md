# FaceLink
Class Project

## Description
Employers often trawl applicants’ social media presences for objectionable behavior. We are creating a business facing application that streamlines the process, combining API data from LinkedIn with that of Facebook and cross referencing them. The difficulty comes down in aligning user profiles with different sets of attributes. For example, given an arbitrary applicant the LinkedIn API might give current city, university, and work history but Facebook might just have the current city and a single item in work history. Being able to match these values and pinpoint specific profiles will take some time and a finely tuned algorithm. We plan to have a solution that will cover at least 80% of the cases, given that certain users don’t have a social media presence or have obfuscated their account details (another issue, applicants changing their Facebook names). This means that for 10 given searches at least 8 queries will return results containing the correct user profile. The final product will have a web-based UI that displays the search results using python to make the API calls and process the data. The search results will display the top five closest results that match the search. Relevant research includes the field of information retrieval.

## Todo's

### Samy
* FB API call function that returns dict

### Dylan
* Linkedin API call function that returns dict

### Paul
* FB user class w/ attributes from dict

### Christina
* Linkedin user class w/ attributes from dict
