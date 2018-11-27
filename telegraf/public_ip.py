#!/usr/bin/env python3
import subprocess
import ipaddress

result = []

result_v4 = subprocess.run(["/usr/bin/curl", "-s4", "me.gandi.net"], capture_output=True, text=True).stdout.strip()
try:
    ipaddress.IPv4Address(result_v4)
    result.append(f'v4="{result_v4}"')
except:
    pass

result_v6 = subprocess.run(["/usr/bin/curl", "-s6", "me.gandi.net"], capture_output=True, text=True).stdout.strip()
try:
    ipaddress.IPv6Address(result_v6)
    result.append(f'v6="{result_v6}"')
except:
    pass

print(f'public_ip {",".join(result)}')
