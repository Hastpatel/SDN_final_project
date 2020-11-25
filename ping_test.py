try:
    import netmiko
    from netmiko import ConnectHandler
    import time
except Exception as e:
    print('Install required modules', e)


user1 = {'device_type': 'cisco_ios', 'password': 'lab123', 'username': 'lab', 'host': '192.168.100.1', 'secret': 'lab123'}
user2 = {'device_type': 'cisco_ios', 'password': 'lab123', 'username': 'lab', 'host': '192.168.100.2', 'secret': 'lab123'}
ping1 = 'ping 2.2.2.2'
ping2 = 'ping 1.1.1.1'
routers = [user1, user2]
ping = [ping1, ping2]


def test():
    for i in range(len(routers)):
        connect = netmiko.ConnectHandler(**routers[i])
        connect.enable()
        aa = connect.send_command(ping[i])
        print(aa)
    return


if __name__ == '__main__':
    test()
