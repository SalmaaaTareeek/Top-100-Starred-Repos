import requests
import json
import os
import urllib.request
import urllib
import collections
BASE = "http://127.0.0.1:5000/"
url = "https://api.github.com/search/repositories?q=created:%3E2020-10-09&sort=stars&order=desc" #can be changeable
response = urllib.request.urlopen(url)
data = json.loads(response.read())
json_data_from_github_api = {}
list_of_names_and_languages = {"name":[],"language":[]}
list_of_languages_with_rep = []
list_of_unique_langs_and_users={"language":[],"users":[]}
list_of_repos_using_specfic_lang = {}
for i in range(len(data["items"])):
    json_data_from_github_api = requests.get(BASE + "/api/" + str(i) + "/" + str(data["items"][i]["name"]) + "/" + str(data["items"][i]["language"]))
    list_of_names_and_languages["name"].append(json_data_from_github_api.json()['name'])
    list_of_names_and_languages["language"].append(json_data_from_github_api.json()['language'])
for j in range(len(list_of_names_and_languages["language"])):
    list_of_languages_with_rep.append(list_of_names_and_languages["language"][j])
for k in list_of_languages_with_rep:
    if k in list_of_unique_langs_and_users["language"]:
        continue
    else:
        list_of_unique_langs_and_users["language"].append(k)
        list_of_unique_langs_and_users["users"].append(list_of_languages_with_rep.count(k))
number_of_repos_used = {k: [] for k in list_of_unique_langs_and_users["language"]}
for iter,m in enumerate(number_of_repos_used.keys()):
    number_of_repos_used[m] = list_of_unique_langs_and_users["users"][iter]
print(number_of_repos_used)
list_of_repos_using_specfic_lang = {k: [] for k in list_of_unique_langs_and_users["language"]}
for m in list_of_repos_using_specfic_lang.keys():
    for iter , n in enumerate(list_of_names_and_languages["language"]):
        if m == n:
            list_of_repos_using_specfic_lang[m].append(list_of_names_and_languages["name"][iter])
# print(list_of_repos_using_specfic_lang)























