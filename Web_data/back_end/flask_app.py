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

commands = ['a', 'a','a', 'a','a', 'a','a', 'a']


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

    print(commands)




class Commands(Resource):

    def post(self):
        reqStr = request.data.decode("utf-8")
        commdList=json.loads(reqStr)
        print(reqStr)
        try:
            for command in commdList:
                strToChar(command)
        except Exception as e:
            print(e)
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
