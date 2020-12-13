from flask import Flask
from flask import render_template
from flask import request
from flask_restful import Resource, Api

from requests import put, get


from back_end.arduino_connection.serial_connection import SerialConn
from back_end.arduino_connection.ajax_response_handeling import Handling

import os


template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)
api = Api(app)

app.static_folder = 'static'
app.secret_key = '!HFEUH!@*$&&$HFIHDS*#@GRIAFHW>?@>MF*W'


# Test


from back_end.Database.personal_project_db_handler import PersonalProjectDbHandler

db_name = 'personal_project_db'
db_table = 'custom_programs'
db_sub_table = 'custom_programs_sub'
db = PersonalProjectDbHandler()
db.init_DB(db_name)
db.db_status()
db.create_table_program_handler(db_table, db_sub_table)
db.new_program(db_table, db_sub_table)


# Globals
global arm_selected
global what_button
global angle_base
global arm_one_angle
global arm_two_angle
global arm_three_angle


# Variables

json_return_eps8266 = {}

# this dictionary will return a list that will look like this: {"example_angle":{"distance": 0,"isReachable":True}, ...}
objects = {}


angleValStr = 0

isClosingStr = False
isUsing_ESP8266 = False

connection_type = "Wifi"
character = ''

handler = Handling()

@app.route('/main_page', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def controles_page_main():
    arm_selected = 1
    what_button = 1

    if request.method == "POST":

        # JSON data decoded from $AJAX
        ajax_json = request.json
        what_button = ajax_json.get('button')
        arm_selected = ajax_json.get('armNum')
        is_closing = ajax_json.get('isClosingArm')
        what_command = ajax_json.get('specialCommands')

        handler.move(
            what_button,
            arm_selected
        )

        handler.grip_arm(
            is_closing
        )

        handler.special_commands(
            what_command
        )

    return render_template('mainWithVideo.html',
                           objects_list=objects
               )



@app.route('/about')
def about_screen():
    return render_template('about.html')


@app.route('/settings')
def setting_screen():
    if request.method == "POST":
        ajax_list = request.json

        is_using_esp8266 = ajax_list.get("isWifiConn")
        connection_type = ajax_list.get("connectionType")
        arduino_esp8266_url = ajax_list.get("arduinoConnUrl")
        connection_method = ajax_list.get("isDebugMode")

    return render_template('settingsFile.html',
                            arduino_conn_link=arduino_esp8266_url
               )


# Handling post requests

@app.route('/post-handling')
def arduino_post_handling():
    if request.method == "POST" and not request:
        incoming_ip = request.remote_addr
        print("POST request from: {}".format(incoming_ip))
        json_return_eps8266 = request

# Handling get requests


class HelloWorld(Resource):

    def __init__(self, character):
        self.char = character

    def get(self):
        return self.char


api.add_resource(HelloWorld(handler.output), '/main_page')

app.run(debug=True)
