#!/usr/bin/env python3

import yaml

filename = input("Enter yaml Filename here: ")
ymfile = input("enter name of newly converted to python file here: ")

with open(filename) as f:
    yaml_out = yaml.load(f)

print(yaml_out)

with open(ymfile, 'wt') as y:
    y.write(str(yaml_out))

