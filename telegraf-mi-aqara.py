#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import json
import subprocess

def on_connect(client, userdata, flags, rc):
    client.subscribe("/homebridge-mi-aqara/+/read_ack")

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode('utf-8'))
        if 'data' in payload:
            data = json.loads(payload['data'])
            fields = []
            for k, v in data.items():
                if k in ['temperature', 'humidity', 'voltage', 'power_consumed', 'inuse', 'rgb', 'illumination']:
                    fields.append('{}={}i'.format(k,v))
                elif k in ['proto_version', 'status']:
                    fields.append('{}="{}"'.format(k,v))
                else:
                    fields.append('{}={}'.format(k,v))
            print('mi-aqara,model={},short_id={},sid={} {}'.format(payload['model'], payload['short_id'], payload['sid'], ','.join(fields)))
    except:
        import traceback
        traceback.print_exc()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)
client.loop_start()

proc = subprocess.Popen(["/path/to/node_modules/.bin/homebridge","-U","/home/user/.homebridge"], stdout=subprocess.DEVNULL)
try:
    proc.wait(timeout=2)
except subprocess.TimeoutExpired:
    proc.kill()
client.loop_stop()
