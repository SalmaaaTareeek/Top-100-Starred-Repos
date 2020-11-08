import requests
import json
import os
import urllib.request
import urllib
BASE = "http://127.0.0.1:5000/"
url = "https://api.github.com/search/repositories?q=created:%3E2020-10-08&sort=stars&order=desc" #can be changeable
max = 0
count = 0
response = urllib.request.urlopen(url)
data = json.loads(response.read())
json_data_from_github_api = {}
list_of_names_and_languages = {"name":[],"language":[]}
list_of_languages = []
for i in range(len(data["items"])-1):
    json_data_from_github_api = requests.get(BASE + "/api/" + str(i) + "/" + str(data["items"][i]["name"]) + "/" + str(data["items"][i]["language"]))
    list_of_names_and_languages["name"].append(json_data_from_github_api.json()['name'])
    list_of_names_and_languages["language"].append(json_data_from_github_api.json()['language'])
for j in range(len(list_of_names_and_languages["language"])):
    list_of_languages.append(list_of_names_and_languages["language"][j])
#print(list_of_languages)












