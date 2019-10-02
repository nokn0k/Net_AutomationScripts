from netmiko import ConnectHandler
from getpass import getpass

cisco = {
	"host": 'cisco3.lasthop.io',
	"username": 'pyclass',
	"password": getpass(),
	"device_type": 'cisco_ios'
}

net_cxn = ConnectHandler(**cisco)
shcmd = net_cxn.send_command("show version")

with open("shversion.txt", "w") as f:
	f.write(shcmd)

net_cxn.disconnect()
