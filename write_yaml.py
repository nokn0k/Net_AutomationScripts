#!/usr/bin/env python3
#For converting a python data structure to yaml
import yaml

my_dict = {
	'device_name': 'router1',
	'ip_addr': '10.1.1.1',
	'username': 'admin',
	'password': 'foo'
}

some_list = list(range(11))
my_dict['some_list'] = some_list
my_dict['null_value'] = None
my_dict['a_bool'] = False

pyfile = input('name of python script to convert: ')
filename = input('name of file to write it to: ')

y=open(pyfile, 'r')
y_contents = y.read()

with open(filename, 'wt') as f:
    yaml.dump(y_contents, f, default_flow_style=False)
