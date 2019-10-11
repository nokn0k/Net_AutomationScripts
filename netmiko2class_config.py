from netmiko import ConnectHandler
from getpass import getpass

#devices = input("enter hostname: ")
#passwd = getpass("Enter hostname user Password:")
command = [
	'logging buffered 18000',
	'clock timezone PST -8 0',
	'no logging console'
]


net_device = {
        "host": 'cisco3.lasthop.io',
        "username": 'pyclass',
        "password": '88newclass',
        "device_type": 'cisco_ios',
	#"global_delay_factor": 4
	#session_log='my_session.txt',
}


device = ConnectHandler(**net_device)
output = device.send_config_from_file(config_file='config1.txt')

print(output)
print(device.find_prompt())
device.disconnect()




