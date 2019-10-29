#!/usr/bin/env python3

from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse
import os
import sys

c_xr = CiscoConfParse('cisco_BGP.txt')
print(c_xr)

