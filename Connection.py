# This code is for python 3 and above 
# You would need to install http.client with pip3 install http.client 

import http.client, urllib.request, urllib.parse, urllib.error
import time
from GPS_API import *
import serial

ser = serial.Serial("/dev/serial0")  # Select your Serial Port
ser.baudrate = 9600  # Baud rate
ser.timeout = 0.5
sleep = 2 # how many seconds to sleep between posts to the channel

key = '9KOZHKZQMMKZ672O'  # Thingspeak Write API Key
msgdata = Message() # Creates a Message Instance

def upload_cloud():
    temp = get_latitude(msgdata)
    temp1 = get_longitude(msgdata)
    params = urllib.parse.urlencode({'field1': temp,'field2': temp1, 'key':key })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept" : "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print(("Lat:",temp))
        print(("Long:",temp1))
        print((response.status, response.reason))
        conn.close()
    except KeyboardInterrupt:
         print("Connection Failed")             
             
if __name__ == "__main__":
    start_gps_receiver(ser, msgdata)
    time.sleep(2)
    ready_gps_receiver(msgdata)
    while True:
        upload_cloud()
        time.sleep(sleep)