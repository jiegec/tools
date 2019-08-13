#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import socket
import struct
import json
import time

MCAST_GRP = '224.0.0.50'
MCAST_PORT = 9898

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((MCAST_GRP, MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

def num(s):
        try:
                return int(s)
        except ValueError:
                return float(s)

client = mqtt.Client()
client.connect('127.0.0.1', 1883, 60)
while True:
    raw_data = sock.recv(10240)
    data = json.loads(raw_data.decode('utf-8'))
    if 'data' in data:
        data.update(json.loads(data['data']))
        del data['data']
    for k, v in data.items():
        if k in ['temperature', 'humidity', 'voltage', 'power_consumed', 'inuse', 'no_motion', 'load_power', 'short_id']:
            data[k] = num(v)
    print(time.asctime(time.localtime(time.time())), data)
    client.publish('/telegraf-mi-aqara', json.dumps(data).encode('utf-8'))
