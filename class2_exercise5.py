from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from datetime import datetime


net_device = {
        "host": 'nxos1.lasthop.io',
        "username": 'pyclass',
        "password": '88newclass',
        "device_type": 'cisco_nxos',
	#"global_delay_factor": 2
	"fast_cli": True
	#session_log='my_session.txt',
}

net_device1 = {
	"host": 'nxos2.lasthop.io',
        "username": 'pyclass',
        "password": '88newclass',
        "device_type": 'cisco_nxos',
       	#"global_delay_factor": 2
        #"fast_cli": True
       	#session_log='my_session.txt',
}

cfg = [
	'ip name-server 1.1.1.1', 
	'ip name-server 1.0.0.1', 
	'ip domain-lookup'
]

start_time = datetime.now()

for x in (net_device, net_device1):
	device = ConnectHandler(**x)
	print(device.find_prompt())
#	output = device.send_config_from_file(config_file='cfg.txt', strip_prompt=False, strip_command=False)
#	save = device.save_config()
	output = device.send_command('show vlan')
	pprint(output)
	#pprint(save)
	device.disconnect()


finish = datetime.now()
dur = finish - start_time
duration = dur.total_seconds()
dur2 = "{:.2f}".format(duration)
duration_str = str(dur2)
print("This script took " + duration_str + "seconds to complete")






