#!/usr/bin/env python3
import subprocess
import re
import os
import sys

miio_id = sys.argv[1]
os.environ["PATH"] += os.pathsep + "/usr/local/bin"
result = subprocess.run(["/usr/local/bin/miio", "inspect", miio_id], capture_output=True, text=True)
flag = False
kv = []
model_info = ''
for line in result.stdout.split('\n'):
    match = re.match('^Model info:\s+([a-zA-Z0-9.]+)$', line)
    if match:
        model_info = match.group(1)
    if flag and line:
        match = re.match('^\s+-\s([a-zA-Z]+):\s(.*)$', line)
        if match.group(1) in ['mode', 'ledBrightness']:
            kv.append(f'{match.group(1)}="{match.group(2)}"')
        else:
            kv.append(f'{match.group(1)}={match.group(2)}')
    if 'Properties:' == line:
        flag = True
print(f'miio,id={miio_id},model_info={model_info} ', end='')
print(','.join(kv))
