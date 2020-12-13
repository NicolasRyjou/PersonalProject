import mysql.connector
import time

class PersonalProjectDbHandler:

    def __init__(self):

        self.host = '127.0.0.1' ###############   CHANGE WHEN PUBLISHING
        self.db_name = "per_prj_db"
        self.user = 'nicolas_ryjoukhine'
        self.password = 'prpjnr'
        self.port = "5000"

        self.db_connection = mysql.connector.connect(
                database=self.db_name,
                host=self.host,
                user=self.user,
                port=self.port,
                passwd=self.password
        )

        self.db_cursor = self.db_connection.cursor()

        self.json_program_name_str = 'name'
        self.json_program_time_str = 'time'
        self.json_program_char_str = 'chars'

    def init_DB(self, db_name):
        print("Careful, do not create new databases when not necessary.")
        try:
            self.db_cursor.execute("CREATE DATABASE {}".format(db_name))
            time.sleep(1)
            print("Database {} create succesfully")

        except Exception as err:
            print("Database creation failed.\nError: {}".format(err))
            return err

    def del_DB(self, db_name):
        try:
            self.db_cursor.execute("DELETE DATABASE {}".format(db_name))
            time.sleep(1)
            print("Database {} create succesfully")

        except Exception as err:
            print("Database deletion failed.\nError: {}".format(err))
            return err

    def db_status(self):
        self.db_cursor.execute("SHOW DATABASES")
        for db in self.db_cursor:
            print("Currently open database: {}")

    def create_table_program_handler(self, table_name, table_sub_name):
        if table_name and table_name:
            try:
                self.db_cursor.execute('CREATE TABLE IF NOT EXISTS {} ('
                                   'id_program INT AUTO_INCREMENT primary key'
                                   'name VARCHAR(255))  NOT null'
                                   'duration INT'
                                   ''.format(table_name)
                                       )
                self.db_cursor.execute('CREATE TABLE IF NOT EXISTS {} ('
                                   'id_connector INT  NOT null'
                                   'character VARCHAR(255))  NOT null'
                                   'request_amount INT'
                                   ''.format(table_sub_name)
                                       )
            except Exception as err:
                print("Error creating table: {}".format(err))
        else:
            print("Please specify both table name and sub table name")

    def checkKey(self, dict, key):
        if key in dict.keys():
            return True
        else:
            print("Key {} not present in json document {}!".format(key, dict))
            return False

    def new_program(self, table_name, table_sub_name, json_doc={}):

        if self.checkKey(json_doc, self.json_program_name_str) and self.checkKey(json_doc, self.json_program_time_str):
            try:
                for prg in len(json_doc.keys()):
                    # inserting into the main DB
                    program_name = json_doc[self.json_program_name_str][prg]
                    program_duration = program_name[self.json_program_time_str]

                    self.db_cursor.execute("INSERT INTO {} (name, duration) VALUES ({}, {})".format(
                        table_name, program_name, program_duration)
                    )

                    # inserting into the sub DB
                    main_table_id_for = self.db_cursor.execute(
                        "SELECT id_program FROM {} WHERE name={}".format(table_name ,program_name)
                    )
                    program_commands = json_doc[self.json_program_name_str][self.json_program_char_str]
                    request_amount = len((program_commands)-1)/2
                    if program_commands:
                        for character in program_commands:
                            self.db_cursor.execute(
                                "INSERT INTO {} (id_connector, character, request_amount) VALUES ({}, {}, {})".format(
                                    table_sub_name,
                                    main_table_id_for,
                                    character,
                                    request_amount
                                )
                            )
                    else:
                        print("No commands available!")
            except Exception as e:
                print("Error: {}".format(e))


        else:
            print("Json document is missing keys."
                  " Please make sure it is in the correct format: "
                  "{{\"name\":name, \"time\":time}, ...}")