import _thread
import time

import serial
import serial.tools.list_ports


class Arduino:

    arduino = 0
    answers = []

    ports=[]
    port=""
    port_set=False

    command = ""
    output_raw = ""
    output_axis = ""
    attitude = ""

    def __init__(self):
        _thread.start_new_thread(self.readArduino, ("Thread-1-read",))

    def getListPort(self):

        ports_raw = serial.tools.list_ports.comports()

        self.ports = []

        print("Ports available: ")
        for port, desc, hwid in sorted(ports_raw):
            print("{}: {} [{}]".format(port, desc, hwid))
            self.ports.append(port)

        return self.ports


    def setPort(self, port):
        if port:
            self.port = port
            try:
                self.arduino = serial.Serial(port=port, baudrate=9600, timeout=.1)
                self.port_set = True
            except:
                pass

    def readArduino(self, thread_name):
        print("Starting " + thread_name)
        while True:
            time.sleep(0.05)
            try:
                if self.port_set:
                    data = self.arduino.readline().decode()
                    if data:
                        print("ARD INPUT -> ", data)
                        self.answers.append(data)

                        # Parsing data
                        if data.startswith("awk"):
                            self.status = data.split()[0].split(":")[1]
                        elif data.startswith("Att"):
                            self.attitude = data.split()[0].split(":")[1]
                        elif data.startswith("Cmd"):
                            self.command = data.split()[0].split(":")[1]
                        elif data.startswith("Out"):
                            self.output_raw = data.split()[0].split(":")[1]
                        elif data.startswith("Axis"):
                            self.output_axis = data.split()[0].split(":")[1]
            except:
                pass

    def writeCommand(self, cmd):
        try:
            if self.port_set:
                self.arduino.write(str.encode(cmd))
        except:
            pass