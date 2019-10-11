from netmiko import ConnectHandler
from getpass import getpass

#devices = input("enter hostname: ")
#passwd = getpass("Enter hostname user Password:")
command = input("Enter command here: ")

net_device = {
        "host": 'cisco3.lasthop.io',
        "username": 'pyclass',
        "password": '88newclass',
        "device_type": 'cisco_ios',
	"global_delay_factor": 4
	#session_log='my_session.txt',
}


device = ConnectHandler(**net_device)
output = device.send_command(command, expect_string=r'filename', 
			    strip_prompt=False, strip_command=False, delay_factor=5)
output += device.send_command('\n', expect_string=r'confirm', 
			    strip_prompt=False, strip_command=False, delay_factor=5)
output += device.send_command('\n')


print(output)
print(device.find_prompt())
device.disconnect()




