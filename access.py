import requests
import json
import os
import urllib.request
import urllib
BASE = "https://api.github.com/search/repositories?q=created:%3E2020-10-07&sort=stars&order=desc" #can be changeable
response = urllib.request.urlopen(BASE)
data = json.loads(response.read())
print(data)




