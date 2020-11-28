try:
    import netmiko
    from netmiko import ConnectHandler
    import regex as re
    import time
except Exception as e:
    print("Install required modules", e)


user = {'device_type': 'linux',
   'ip': '192.168.56.107',
   'password': 'mininet',
   'username': 'mininet',
    'secret':'mininet'}
# print(user)
user_sdn = {'device_type': 'linux',
   'ip': '192.168.56.108',
   'password': 'sdn',
   'username': 'sdn',
    'secret':'sdn'}

def sdn_controller():
    sdn_conn = netmiko.ConnectHandler(**user_sdn)
    sdn_conn.enable()
    sdn = 'ryu-manager ryu/ryu/app/simple_switch_13.py'
    ryu_controller = sdn_conn.send_command_timing(sdn)
    if 'Password:' in ryu_controller:
        ryu_controller += sdn_conn.send_command_timing('sdn')
    print(ryu_controller)
    return

connect_main = netmiko.ConnectHandler(**user)
connect_main.enable()

def mininet_init():
   mini='sudo mn'
   mininet=connect_main.send_command_timing(mini)
   if 'Password:' in mininet:
      mininet+=connect_main.send_command_timing('mininet')
   #print(mininet)
   return

def controller_config():
   mininet2=connect_main.send_command_timing('sh ovs-vsctl set bridge s1 protocols=OpenFlow13'+'\n'+'sh ovs-vsctl set-controller s1 tcp:10.20.30.2:6633')
   #print(mininet2)
   return

def pingall():
   mininet3=connect_main.send_command_timing('pingall')
   #print(mininet3)
   return

def controller_connectivity():
   show='sudo ovs-vsctl show'
   connect3=netmiko.ConnectHandler(**user)
   connect3.enable()
   see=connect3.send_command_timing(show)
   if 'Password:' in see:
      see+=connect3.send_command_timing('mininet')
   print(see)
   connect3.disconnect()
   return


if __name__=='__main__':
   sdn_controller()
   mininet_init()
   controller_config()
   controller_connectivity()
   #pingall()

