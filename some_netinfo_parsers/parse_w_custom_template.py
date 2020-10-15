#!/usr/bin/python3

# Example of receiving and processing data using custom template and textfsm

import yaml
import textfsm
import myworkfuncs
from tabulate import tabulate
 
if __name__ == '__main__':

    devices = yaml.safe_load(open('mydevices.yaml'))
    all_done = myworkfuncs.threads_conn('connect_ssh', devices['routers'], command='sh ver')

    cli_table = textfsm.clitable.CliTable('index', '/home/user/templates/')
    attributes = {'Command': 'show version', 'Vendor': 'cisco_ios'}

    for item in all_done:
        for crouter in item:
            cli_table.ParseCmd(item[crouter], attributes)
            print(item[crouter])
            print('Formatted Table:\n', cli_table.FormattedTable())
        print()
