import requests
import json
import os
import urllib.request
import urllib
BASE = "http://127.0.0.1:5000/"
url = "https://api.github.com/search/repositories?q=created:%3E2020-10-08&sort=stars&order=desc" #can be changeable
response = urllib.request.urlopen(url)
data = json.loads(response.read())
json_data_from_github_api = {}
list_of_names_and_languages = {"name":[],"language":[]}
print(data["items"][0]["language"]) #accessing specfic Language
print(type(data["items"][0]["language"]))
for i in range(len(data["items"])-1):
    json_data_from_github_api = requests.get(BASE + "/api/" + str(i) + "/" + str(data["items"][i]["name"]) + "/" + str(data["items"][i]["language"]))
    list_of_names_and_languages["name"].append(json_data_from_github_api.json()['name'])
    list_of_names_and_languages["language"].append(json_data_from_github_api.json()['language'])

print(list_of_names_and_languages)







