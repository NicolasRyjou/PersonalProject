from serial import Serial

import serial.tools.list_ports


class SerialConn:

    def __init__(self):
        self.serial_port = "COM7"
        self.baud_rate = 9600
        self.timeout = 0.1
        self.encode_method = 'ascii'
        self.decode_method = 'UTF-8'

        self.serial_conn = Serial(
            self.serial_port,
            self.baud_rate,
            timeout=self.timeout
        )

    def get_available_ports(self):
        ports = [serial.tools.list_ports.comports()]

        print("Serial communications currently open: {}".format(ports))

        return ports

    def write_serial_port(self, content):
        if content and type(content) == "str":

            if not self.serial_conn.isOpen():
                self.serial_conn.open()

            self.serial_conn.write(content.encode(
                    self.encode_method
                )
            )

    def read_serial_port(self):
        if self.serial_conn.readable():
            incoming_content = self.serial_conn.read().decode(
                self.decode_method
            )
            if not incoming_content == "hc04data_start":
                return incoming_content

            else:
                return_json = {}

                angleValStr = 1

                print("Reading HC 04 data")

                while not incoming_content == "hc04data_end":

                    incoming_content = self.serial_conn.read().decode(
                        self.decode_method
                    )

                    temporaryDict = {
                        "distance": 0,
                        "isReachable": False
                    }

                    temporaryDict["distance"] = incoming_content
                    if incoming_content <= 20:
                        temporaryDict["isReachable"] = True
                    else:
                        temporaryDict["isReachable"] = False

                    return_json["angle_{}".format(str(angleValStr))] = temporaryDict

                    angleValStr += 1

                return return_json




