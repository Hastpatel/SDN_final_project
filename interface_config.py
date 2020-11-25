#!/usr/bin/env python3

try:
    import netmiko
    from netmiko import ConnectHandler
    import json

except Exception as e:
    print('Install required modules', e)

user1 = {'device_type': 'cisco_ios', 'password': 'lab123', 'username': 'lab', 'host': '192.168.100.1', 'secret': 'lab123'}
user2 = {'device_type': 'cisco_ios', 'password': 'lab123', 'username': 'lab', 'host': '192.168.100.2', 'secret': 'lab123'}

interface1 = ['int fa0/0', 'ip address 10.0.0.1 255.255.255.0', 'no shut']
loopback1 = ['int lo1', 'ip address 1.1.1.1 255.255.255.0', 'no shut']
interface2 = ['int fa0/0', 'ip address 10.0.0.2 255.255.255.0', 'no shut']
loopback2 = ['int lo1', 'ip address 2.2.2.2 255.255.255.0', 'no shut']

routers = [user1, user2]
iface = [interface1, interface2]
loop = [loopback1, loopback2]


def get_ips():
    interfaces = {'R1': {}, 'R2': {}}
    for i in range(len(routers)):
        conn = netmiko.ConnectHandler(**routers[i])
        conn.enable()
        conn.send_config_set(iface[i])
        conn.send_config_set(loop[i])
        out = conn.send_command('sh ip int brief')
        out = out.split('\n')
        conn.disconnect()
        for k in interfaces:
            for j in range(len(out)):
                a = out[j].split()
                if a[4] == 'up':
                    interfaces[k][a[0]] = a[1]
    return interfaces


if __name__ == '__main__':
    print(get_ips())
