from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from datetime import datetime
import time

net_device = {
        "host": 'cisco4.lasthop.io',
        "username": 'pyclass',
        "password": '88newclass',
        "secret": '88newclass',
	"device_type": 'cisco_ios',
	"session_log":'my_cmd_logs.txt'
}

start_time = datetime.now()

device = ConnectHandler(**net_device)
print(device.find_prompt())
output = device.config_mode()
print(device.find_prompt())
output = device.exit_config_mode()
print(device.find_prompt())
print(device.write_channel('disable\n'))
time.sleep(2)
print(device.read_channel())
print(device.find_prompt())
print(device.enable())
print(device.find_prompt())

#pprint(output)
device.disconnect()


finish = datetime.now()
dur = finish - start_time
duration = dur.total_seconds()
dur2 = "{:.2f}".format(duration)
duration_str = str(dur2)
print("This script took " + duration_str + "seconds to complete")






