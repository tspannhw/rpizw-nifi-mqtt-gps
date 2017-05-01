#! /usr/bin/python
# Based on
# Written by Dan Mandle http://dan.mandle.me September 2012
# License: GPL 2.0

import os
from gps import *
from time import *
import time
import threading
import json
import paho.mqtt.client as paho

gpsd = None 

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true

  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer

if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    while True:
      if gpsd.fix.latitude > 0:
        row = [ { 'latitude': str(gpsd.fix.latitude),
         'longitude': str(gpsd.fix.longitude),
         'utc': str(gpsd.utc),
         'time':   str(gpsd.fix.time),
         'altitude': str(gpsd.fix.altitude),
         'eps': str(gpsd.fix.eps),
         'epx': str(gpsd.fix.epx),
         'epv': str(gpsd.fix.epv),
         'ept': str(gpsd.fix.ept),
         'speed': str(gpsd.fix.speed),
         'climb': str(gpsd.fix.climb),
         'track': str(gpsd.fix.track),
         'mode': str(gpsd.fix.mode)} ]

        json_string = json.dumps(row)
        client = paho.Client()
        client.username_pw_set("jrfcwrim","UhBGemEoqf0D")
        client.connect("m13.cloudmqtt.com", 14162, 60)
        client.publish("rpiwzgps", payload=json_string, qos=0, retain=True)

        time.sleep(60)

  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
