from netmiko import ConnectHandler
from getpass import getpass

passwd = getpass()

device_1 = {
	"host": 'nxos2.lasthop.io',
	"username": 'pyclass',
	"password": passwd,
	"device_type": 'cisco_nxos'
	#session_log='my_session.txt',
}

device_2 = {
	"host": 'nxos1.lasthop.io',
	"username": 'pyclass',
	"password": passwd,
	"device_type": 'cisco_nxos'
}

for x in (device_1, device_2):
	device = ConnectHandler(**x)
	print(device.find_prompt())

