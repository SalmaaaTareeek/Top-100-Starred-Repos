import requests
import urllib.request
BASE = "https://api.github.com/search/repositories?q=created:%3E2020-10-07&sort=stars&order=desc" #can be changeable
file = open("api.json", "w" , encoding='utf-8')
for line in urllib.request.urlopen(BASE):
    readable = line.decode('utf-8')
    file.write(readable+"\n")
    file.close()


