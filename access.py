import requests
import json
import os
import urllib.request
import urllib
import collections
BASE = "http://127.0.0.1:5000/"  #url of the local server
url = "https://api.github.com/search/repositories?q=created:%3E2020-10-09&sort=stars&order=desc" #can be changeable (URL of github api)
response = urllib.request.urlopen(url) #requests the Data from Url
data = json.loads(response.read())     #read the data from url
json_data_from_github_api = {}         #empty dict to get the json data from github api
list_of_names_and_languages = {"name":[],"language":[]}  #empty dict to store lists of repos and languages used
list_of_languages_with_rep = []    #empty lists of all languages used in repos shown in api
list_of_unique_langs_and_users={"language":[],"users":[]}      #emptidict that lists the language used with the number of users used it
list_of_repos_using_specfic_lang = {}         #empty dict to list users using specfic language
#this loop will get the data from url passed from the server
for i in range(len(data["items"])):
    json_data_from_github_api = requests.get(BASE + "/api/" + str(i) + "/" + str(data["items"][i]["name"]) + "/" + str(data["items"][i]["language"]))
    list_of_names_and_languages["name"].append(json_data_from_github_api.json()['name'])
    list_of_names_and_languages["language"].append(json_data_from_github_api.json()['language'])
#this loop will get all the languages with repetetion given from the api
for j in range(len(list_of_names_and_languages["language"])):
    list_of_languages_with_rep.append(list_of_names_and_languages["language"][j])
#this loop will get the number of users using specfic languages
for k in list_of_languages_with_rep:
    if k in list_of_unique_langs_and_users["language"]:
        continue
    else:
        list_of_unique_langs_and_users["language"].append(k)
        list_of_unique_langs_and_users["users"].append(list_of_languages_with_rep.count(k))
number_of_repos_used = {k: [] for k in list_of_unique_langs_and_users["language"]}
#this loop will get too number of users using specfic languages but in format of (key:value) ex:("python":3)
for iter,m in enumerate(number_of_repos_used.keys()):
    number_of_repos_used[m] = list_of_unique_langs_and_users["users"][iter]
#this loop will get the list of names of repos used the specfic lang ex("python":[x,y,z])
list_of_repos_using_specfic_lang = {k: [] for k in list_of_unique_langs_and_users["language"]}
for m in list_of_repos_using_specfic_lang.keys():
    for iter , n in enumerate(list_of_names_and_languages["language"]):
        if m == n:
            list_of_repos_using_specfic_lang[m].append(list_of_names_and_languages["name"][iter])
print("List of languages used:")
print(list_of_unique_langs_and_users["language"])
print("Number of users using each language:")
print(number_of_repos_used)
print("Names of repos used for each language:")
print(list_of_repos_using_specfic_lang)
























