#!/usr/bin/env python3

import json

filename = input("Enter yaml Filename here: ")
jsfile = input("enter name of newly converted to python file here: ")

with open(filename) as f:
    json_out = json.load(f)

print(json_out)

with open(jsfile, 'wt') as y:
    y.write(str(json_out))

