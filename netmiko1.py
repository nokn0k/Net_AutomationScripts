from netmiko import ConnectHandler
from getpass import getpass

device_1 = {
	"host": 'cisco3.lasthop.io',
	"username": 'pyclass',
	"password": getpass(),
	"device_type":'cisco_ios',
	#session_log='my_session.txt',
}

device_1 = ConnectHandler(**device_1)

print(device_1.find_prompt())
