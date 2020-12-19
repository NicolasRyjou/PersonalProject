from flask import Flask
from flask import request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

commands = []


class Commands(Resource):

    def post(self):
        char = request.form['data']
        commands.append(char)
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

api.add_resource(Commands, '/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
