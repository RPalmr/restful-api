from flask_restful import Resource
from flask import request

class Register(Resource):
    def get(self):
        return { "message" : "getting user"}

    def post(self):
        data = request.get_json()
        print(data['password'])
        username = data['username']
        location = data['location']
        password = data['password']
        email = data['email']
        return { "message" : "registering {}".format(username) }