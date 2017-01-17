#!/usr/bin/env python

import sys
import json
from influxdb import InfluxDBClient
import subprocess

p = subprocess.Popen(["/opt/speedtest-cli/speedtest.py", "--json"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = p.communicate()

errors = []
j = None
if stderr is not None and stderr != "":
    print("Got error {}".format(stderr))
    errors.append(stderr)

try:
    j = json.loads(stdout)
except ValueError as e:
    print("Got error {}".format(str(e)))
    errors.append(str(e))

data = []

if j:
    data.append({
        "measurement": "download_speed",
        "fields": {
            "speed": j["download"]
        }
    })
    data.append({
        "measurement": "upload_speed",
        "fields": {
            "speed": j["upload"]
        }
    })
    data.append({
        "measurement": "ping",
        "fields": {
            "latency": j["ping"]
        }
    })

for e in errors:
    data.append({
        "measurement": "errors",
        "fields": {
            "message": str(e)
        }
    })

print("Writing to DB:\n{}".format(data))

influx = InfluxDBClient("127.0.0.1", 8086, "admin", "admin", "stats")
influx.write_points(data)
