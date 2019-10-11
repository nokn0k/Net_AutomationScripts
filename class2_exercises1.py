from netmiko import ConnectHandler
from getpass import getpass

#devices = input("enter hostname: ")
#passwd = getpass("Enter hostname user Password:")
#command = [
#	'logging buffered 18000',
#	'clock timezone PST -8 0',
#	'no logging console'
#]


net_device = {
        "host": 'cisco4.lasthop.io',
        "username": 'pyclass',
        "password": '88newclass',
        "device_type": 'cisco_ios',
	#"global_delay_factor": 4
	#session_log='my_session.txt',
}


device = ConnectHandler(**net_device)
output = device.send_command('ping', expect_string=r'Protocol', strip_prompt=False, strip_command=False)
output += device.send_command('\n', expect_string=r'Target', strip_prompt=False, strip_command=False)
output += device.send_command('8.8.8.8', expect_string=r'Repeat', strip_prompt=False, strip_command=False)
output += device.send_command('\n', expect_string=r'Datagram', strip_prompt=False, strip_command=False)
output += device.send_command('\n', expect_string=r'Timeout', strip_prompt=False, strip_command=False)
output += device.send_command('\n', expect_string=r'Extended', strip_prompt=False, strip_command=False)
output += device.send_command('\n', expect_string=r'Sweep', strip_prompt=False, strip_command=False)

print(output)
print(device.find_prompt())
device.disconnect()




