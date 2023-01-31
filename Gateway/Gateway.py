import serial
import time
import requests
import sys


port = sys.argv[1]
url = sys.argv[2]

port_serie = serial.Serial(port = "COM4", baudrate = 9600)
print(port_serie.readline())
print("Gonna query server: " + url)
print("Trying to open port on " + port)
port_serie.flushInput()
port_serie.flushOutput()
while True :
    try:
        print(port_serie.readline())
        port_serie = port_serie.decode(encoding='UTF-8',errors='strict')
        port_serie = port_serie.read()
        val = ord(port_serie)
        port_serie = requests.post(url + "/values", json={"value": val})
    except Exception as e :
        print("Error occurred!\n" + str(e))

    finally :
        time.sleep(2)

        
    port_serie.close()

