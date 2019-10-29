#!/usr/bin/env python

from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse


dev = {
 'device_type': 'cisco_ios',
 'host': 'cisco4.lasthop.io',
 'username': 'pyclass',
 'password': '88newclass'
}

x = ConnectHandler(**dev)

cfg = x.send_command('sh run')
cmd = CiscoConfParse(cfg.splitlines())

int = cmd.find_objects_w_child(parentspec=r'interface', childspec=r'^\s+ip address')

for x in int:
    ip_x = x.re_search_children(r'ip address')[0].text
    print()
    print('Interface is {}'.format(x.text))
    print('IP address is {}'.format(ip_x))
    print()
