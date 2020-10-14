#!/usr/bin/env python

from concurrent.futures import ProcessPoolExecutor
from itertools import repeat
import yaml
from netmiko import ConnectHandler
from textfsm import clitable
import textfsm
from tabulate import tabulate

# My multiconnection functions
def connect_ssh(device_dict, command):
    with ConnectHandler(**device_dict) as ssh:
        result = ssh.send_command(command)
        print ('Working with {} ...'.format(device_dict['ip']))
    return {device_dict['ip']: result}

def threads_conn(function, devices, limit=2, command=''):
    with ProcessPoolExecutor(max_workers=limit) as executor:
        f_result = executor.map(function, devices, repeat(command))
    return list(f_result)

if __name__ == '__main__':

# Example how to use multiconnection function
    devices = yaml.safe_load(open('devices.yaml'))
    all_done = threads_conn(connect_ssh, devices['routers'], command='sh ver')

    with open("cisco_ios_show_version.textfsm") as f:
        re_table = textfsm.TextFSM(f)
    header = re_table.header

    for item in all_done:
        for crouter in item:
            print(item[crouter])
            result = re_table.ParseText(item[crouter])
            print(tabulate(result, headers=header))
        print()