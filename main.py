from flask import Flask,request
from flask_restful import Api, Resource,reqparse,abort
import requests
import urllib.request
#  to create an app using flask
app = Flask(__name__)
api = Api(app)
github_data = {}
class repos(Resource):
    def get(self,repo_id,name,language):
        return {"ID":repo_id,"name":name,"language":language}

api.add_resource(repos,"/api/<string:repo_id>/<string:name>/<string:language>")
# to run the application
if __name__ == "__main__":
    app.run(debug=True)  #debuggind mode menans testing mode as a developer not a production




