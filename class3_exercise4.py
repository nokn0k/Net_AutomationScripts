#!/usr/bin/env python3

import json

filename = 'json_sample2.json'

with open(filename) as j:
    json_out = json.load(j)

json_out = json_out['ipV4Neighbors']

d = {}

for x in json_out:
    ip = x['address']
    mac = x['hwAddress']
    d[ip] = mac
print(d)

