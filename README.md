# Top-100-Starred-Repos
Developing a REST microservice that list the languages used by the 100 trending public repos on GitHub.

Description of the project:

Develop a REST microservice that list the languages used by the 100 trending public repos on GitHub:
For every language, you need to calculate the attributes below:
* Number of repos using this language.
* The list of repos using the language.
Fetching trending repositories simply translates to fetching the most starred repos created in the last 30 days ( from now ). To do that, you'll need to call the following endpoint:

Standard: (and you can Change the date to be 30 days from now)
https://api.github.com/search/repositories?q=created:>{date}&sort=stars&order=desc

Example used in our project and can be changed:
https://api.github.com/search/repositories?q=created:%3E2020-10-09&sort=stars&order=desc

Version1 Release:

The code of the project will work dynamically with any date and API has the same specs.
This endpoint returns 30 repos so it returns 30 repos with their languages and for each language will returns:
* Number of repos using this language.
* The list of repos using the language.

Requirements:

When cloning the repo at your local PC:
* Open CMD/Anaconda/Python Terminal in specific folder
* pip install –r req.txt
* pip install json
* pip install urllib.request
* pip install urllib
* pip install collections
* And this will install all the libraries needed

Technologies and web framework and language used:

* Flask framework
* Python Programming Language

Steps for the files in the project:


1. Open main.py and run this will be the server that I will get the parameters and method from it.
2. Then open access.py and run.
3. The printed output will be:
* List Of Languages Used in the returned repos
* Number of users used each language ex. (“Python:3”)
* Names of users used specific Language ex. (“Python:[x,y,z]”)


 
