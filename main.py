from flask import Flask,request
from flask_restful import Api, Resource,reqparse,abort
import requests
import urllib.request
#  to create an app using flask
app = Flask(__name__)
api = Api(app)
github_data = {}
class repos(Resource):
    #this function will get the repo_id which will be initialized with 0
    #name will got the name of the repo
    #language will got the language used in repos
    def get(self,repo_id,name,language):
        return {"ID":repo_id,"name":name,"language":language}
#will pass the repo ID and name and language to the class and then this will get accessed by access.py
api.add_resource(repos,"/api/<string:repo_id>/<string:name>/<string:language>")
# Initializing the server
if __name__ == "__main__":
    app.run(debug=False)  #debuggind mode menans testing mode as a developer not a production




