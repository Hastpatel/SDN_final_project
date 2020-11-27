#!/usr/bin/env python3

try:
    import netmiko
    from netmiko import ConnectHandler
    import json
except Exception as e:
    print('Install required modules', e)

user1 = {'device_type': 'cisco_ios', 'password': 'lab123', 'username': 'lab', 'host': '192.168.100.1', 'secret': 'lab123'}
user2 = {'device_type': 'cisco_ios', 'password': 'lab123', 'username': 'lab', 'host': '192.168.100.2', 'secret': 'lab123'}

ospf1 = ['router ospf 1', 'network 1.1.1.1 0.0.0.255 area 0', 'network 10.0.0.1 0.0.0.255 area 0', 'network 10.20.50.1 0.0.0.255 area 0']
ospf2 = ['router ospf 1', 'network 2.2.2.2 0.0.0.255 area 0', 'network 10.0.0.2 0.0.0.255 area 0', 'network 10.20.30.1 0.0.0.255 area 0']

routers = [user1, user2]
ospf = [ospf1, ospf2]


def ospf_conf():
    for i in range(len(routers)):
        conn = netmiko.ConnectHandler(**routers[i])
        conn.enable()
        conn.send_config_set(ospf[i])
        out = conn.send_command('sh run | section ospf')
        print(out)
        conn.disconnect()
    return


if __name__ == '__main__':
    ospf_conf()
