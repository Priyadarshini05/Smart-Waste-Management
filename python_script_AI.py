import json
import requests
import sys
import os
import paho.mqtt.client as mqtt
import time


# Function which get's triggered when connection is established
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))
    print('Connected')
    client.subscribe("bin/threshold/input", 1)


# This function is callback for message
def on_message(client, userdata, msg):
    # response = msg.payload
    print("message")
    print(msg.payload)
    if msg.payload.decode() == "bin1Full":
        func1()
        fileopen1()

    elif msg.payload.decode() == "bin2Full":
        func2()
        fileopen2()


# Function which get's called when connection is established to subscribe to a topic
def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
    return


# function to publish message to Mosquitto
def publish_data1():
    print('inside publish')
    client.publish('bin/threshold/output/1', "bin1FullOutput")
    print("Data Published")
    time.sleep(1)


# function to publish message to Mosquitto
def publish_data2():
    print('inside publish')
    client.publish('bin/threshold/output/2', "bin2FullOutput")
    print("Data Published")
    time.sleep(1)


# function to post problem and domain file when particular message is subscribed
def func1():
    data = {'domain': open(sys.argv[1], 'r').read(),
            'problem': open(sys.argv[2], 'r').read()}
    response = requests.post('http://solver.planning.domains/solve', json=data).json()
    with open(sys.argv[4], 'w') as f:
        for act in response['result']['plan']:
            f.write('\n')
            f.write(str(act['name']))


# function to post problem and domain file when particular message is subscribed
def func2():
    data = {'domain': open(sys.argv[1], 'r').read(),
            'problem': open(sys.argv[3], 'r').read()}
    response = requests.post('http://solver.planning.domains/solve', json=data).json()
    with open(sys.argv[4], 'w') as f:
        for act in response['result']['plan']:
            f.write('\n')
            f.write(str(act['name']))


# function to write the plan to a plan.txt file and read the file for particular keyword
def fileopen1():
    f = open("plan.txt", "r")
    first_line = f.readline()
    second_line = f.readline()
    third_line = f.readline()
    print("fileopen")

    if second_line[1] == 'w' and second_line[16] == '1':
        if third_line[1] == 'd' and third_line[5] == 'n' and third_line[19] == '2':
            publish_data1()

    f.close()


# function to write the plan to a plan.txt file and read the file for particular keyword
def fileopen2():
    f = open("plan.txt", "r")
    first_line = f.readline()
    second_line = f.readline()
    third_line = f.readline()

    if second_line[1] == 'w' and second_line[5] == 'n' and second_line[19] == '1':
        if third_line[1] == 'd' and third_line[16] == '2':
            publish_data2()

    f.close()


client = mqtt.Client()
client.connect("192.168.0.106", 1883, 60)
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.loop_forever()
