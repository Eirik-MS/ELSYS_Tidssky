#
# Created by Rui Santos
# Complete project details: http://randomnerdtutorials.com
#

import paho.mqtt.client as mqtt

mqttc=mqtt.Client()
mqttc.connect("localhost",1883,60)
mqttc.loop_start()
timer_startwifi = "home/timer/start"


def action(board, changePin, action):
      mqttc.publish(pins[changePin]['topic'],"1")



if __name__ == "__main__":
   
