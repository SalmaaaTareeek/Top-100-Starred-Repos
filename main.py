from flask import Flask,request
from flask_restful import Api, Resource,reqparse,abort
import requests

#  to create an app using flask
app = Flask(__name__)
api = Api(app)


# api.add_resource(Video,"/video/<int:video_id>")




# to run the application
if __name__ == "__main__":
    app.run(debug=True)  #debuggind mode menans testing mode as a developer not a production




