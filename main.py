from flask import Flask,request
from flask_restful import Api, Resource,reqparse,abort
import requests
import urllib.request
#  to create an app using flask
app = Flask(__name__)
api = Api(app)
#For parsing data in json file exported from the github api
repo_add_args = reqparse.RequestParser()
repo_add_args.add_argument("name",type=str , help="" , required=True)
repo_add_args.add_argument("language",type=str , help="",required=True)
# repo_add_args.add_argument("repo_id",type=int , help="",required=True)
github_data = {}
class repos(Resource):
    def get(self,repo_id,name,language):
        return {"ID":repo_id,"name":name,"language":language}

api.add_resource(repos,"/api/<int:repo_id>/<string:name>/<string:language>")




# to run the application
if __name__ == "__main__":
    app.run(debug=True)  #debuggind mode menans testing mode as a developer not a production




