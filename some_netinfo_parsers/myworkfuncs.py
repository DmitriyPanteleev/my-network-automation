#!/usr/bin/env python

# My working functions
from concurrent.futures import ProcessPoolExecutor
from itertools import repeat
from netmiko import ConnectHandler

def connect_ssh(device_dict, command):
    with ConnectHandler(**device_dict) as ssh:
        result = ssh.send_command(command)
        print ('Working with {} ...'.format(device_dict['ip']))
    return {device_dict['ip']: result}

def threads_conn(function, devices, limit=2, command=''):
    with ProcessPoolExecutor(max_workers=limit) as executor:
        f_result = executor.map(function, devices, repeat(command))
    return list(f_result)
