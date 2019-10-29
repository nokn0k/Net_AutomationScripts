#!/usr/bin/env python3

import yaml
from netmiko import ConnectHandler

filename = '.netmiko.yml'

with open(filename) as f:
    yaml_out = yaml.load(f)

device = yaml_out['cisco3']

conn = ConnectHandler(**device)
y = conn.find_prompt()

print()
print(y)
print()

