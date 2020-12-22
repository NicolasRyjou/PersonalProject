from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
import json

app = Flask(__name__)
CORS(app, origins="http://127.0.0.1:4200", allow_headers=[
        "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
        supports_credentials=True)
api = Api(app)

commands = []

def strToChar(string: str):
    if(string == "Move second arm up"):
        commands.append('a')
    if (string == "Move first arm up"):
        commands.append('b')
    if (string == "Toggle Spade Off"):
        commands.append('c')
    if (string == "Toggle Spade On"):
        commands.append('d')
    if (string == "Move first arm down"):
        commands.append('e')
    if (string == "Move second arm down"):
        commands.append('f')
    if (string == "Move crane left"):
        commands.append('g')
    if (string == "Move crane right"):
        commands.append('h')
    else:
        jsonDoc = json.dumps(string)
        for obj in jsonDoc["commands"]:
            print(obj)
            temp = strToChar(obj)
            commands.append(temp)
    print(commands)




class Commands(Resource):

    def post(self):
        char = request.form["data"]
        print(char)
        strToChar(char)
        return json.dumps(commands)

    def get(self):
        if len(commands) > 0:
            char = commands[0]
            commands.remove(char)
            return char
        return ''

    def delete(self):
        commands = []
        return '', 204

api.add_resource(Commands, '/com')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
