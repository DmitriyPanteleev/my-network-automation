#!/usr/bin/python3

# Example of receiving and processing data using textfsm

import yaml
import textfsm
import myworkfuncs
from tabulate import tabulate

if __name__ == '__main__':

    devices = yaml.safe_load(open('mydevices.yaml'))
    all_done = myworkfuncs.threads_conn('connect_ssh', devices['routers'], command='sh ver')

    with open("cisco_ios_sh_ver_custom.textfsm") as f:
        re_table = textfsm.TextFSM(f)
    header = re_table.header

    for item in all_done:
        for crouter in item:
            print(item[crouter])
            result = re_table.ParseText(item[crouter])
            print(tabulate(result, headers=header))
        print()
