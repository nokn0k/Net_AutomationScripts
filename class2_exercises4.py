from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
from datetime import datetime


#devices = input("enter hostname: ")
#passwd = getpass("Enter hostname user Password:")
#command = [
#	'logging buffered 18000',
#	'clock timezone PST -8 0',
#	'no logging console'
#]


net_device = {
        "host": 'cisco3.lasthop.io',
        "username": 'pyclass',
        "password": '88newclass',
        "device_type": 'cisco_ios',
	#"global_delay_factor": 2
	"fast_cli": True
	#session_log='my_session.txt',
}

cfg = [
	'ip name-server 1.1.1.1', 
	'ip name-server 1.0.0.1', 
	'ip domain-lookup'
]

start_time = datetime.now()
device = ConnectHandler(**net_device)
print(device.find_prompt())
#output = device.send_command('show lldp neighbors detail')
output = device.send_config_set(cfg, strip_prompt=False, strip_command=False)
output += device.send_command('ping google.com', strip_prompt=False, strip_command=False)
#output = device.send_command('ping', expect_string=r'Protocol', strip_prompt=False, strip_command=False)
#output += device.send_command('\n', expect_string=r'Target', strip_prompt=False, strip_command=False)
#output += device.send_command('8.8.8.8', expect_string=r'Repeat', strip_prompt=False, strip_command=False)
#output += device.send_command('\n', expect_string=r'Datagram', strip_prompt=False, strip_command=False)
#output += device.send_command('\n', expect_string=r'Timeout', strip_prompt=False, strip_command=False)
#output += device.send_command('\n', expect_string=r'Extended', strip_prompt=False, strip_command=False)
#output += device.send_command('\n', expect_string=r'Sweep', strip_prompt=False, strip_command=False)

pprint(output)
device.disconnect()
finish = datetime.now()
dur = finish - start_time
duration = dur.total_seconds()
dur2 = "{:.2f}".format(duration)
duration_str = str(dur2)
print("This script took " + duration_str + "seconds to complete")






