import time
import paho.mqtt.client as mqtt

MQTT_ADDRESS = '192.168.216.64'
MQTT_USER = 'host'
MQTT_PASSWORD = 'host'
MQTT_TOPIC = 'home/+/+'


def on_connect(client, userdata, flags, rc):
    """ The callback for when the client receives a CONNACK response from the server."""
    print('Connected with result code ' + str(rc))
    client.subscribe(MQTT_TOPIC)

def send_message(client):
    print("trying to send message")
    if (client.publish('home/timer/start', 'hello world')):
        print("message sent")
    else:
        print("message failed")


def on_message(client, userdata, msg):
    """The callback for when a PUBLISH message is received from the server."""
    print(msg.topic + ' ' + str(msg.payload))
    


def main():
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect(MQTT_ADDRESS, 1883)
    mqtt_client.loop_forever()

    while True:
        send_message(mqtt_client)
        time.sleep(20)
        


if __name__ == '__main__':
    print('MQTT to InfluxDB bridge')
    main()

"""
    Debug output:
    0: Connection successful
    1: Connection refused   incorrect protocol version
    2: Connection refused   invalid client identifier
    3: Connection refused   server unavailable
    4: Connection refused   bad username or password
    5: Connection refused   not authorized
    6-255: Currently unused.
"""