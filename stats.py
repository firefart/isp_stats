#!/usr/bin/env python

import json
from influxdb import InfluxDBClient
import subprocess

DATABASE = "{{ db_name }}"
DB_USER = "{{ influxdb_username }}"
DB_PW = "{{ influxdb_password }}"
SPEEDTEST = "{{ speedtest_cli_path }}/speedtest.py"

print("Starting Speedtest...")
p = subprocess.Popen([SPEEDTEST, "--json"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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

# sample data
# server": {"latency": 17.473, "name": "Vienna", "url": "http://speedtest.nessus.at/speedtest/upload.php", "country": "Austria", "lon": "16.3726", "cc": "AT", "host": "speedtest.nessus.at:8080", "sponsor": "Nessus GmbH (10G Uplink)", "url2": "http://speedtest2.nessus.at/speedtest/upload.php", "lat": "48.2088", "id": "3744", "d": 1.3292411343362884}}

if j:
    data.append({
        "measurement": "speedtest",
        "tags": {
            "server_id": j["server"]["id"],
            "server_name": j["server"]["name"],
            "server_host": j["server"]["host"],
            "server_sponsor": j["server"]["sponsor"],
            "server_latency": j["server"]["latency"],
            "server_url": j["server"]["url"],
            "server_url2": j["server"]["url2"],
            "server_country": j["server"]["country"],
            "server_cc": j["server"]["cc"],
            "server_lon": j["server"]["lon"],
            "server_lat": j["server"]["lat"],
            "server_d": j["server"]["d"]
        },
        "fields": {
            "download_speed": j["download"],
            "upload_speed": j["upload"],
            "ping": j["ping"]
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

influx = InfluxDBClient("127.0.0.1", 8086, DB_USER, DB_PW, DATABASE)
influx.write_points(data)
