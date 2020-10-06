
import time
import subprocess
from concurrent.futures import ProcessPoolExecutor
from pprint import pprint
from datetime import datetime
from itertools import repeat
from netmiko import ConnectHandler

def ping_ip(ip_address = '127.0.0.1', count = 3):
    reply = subprocess.run('ping -c {count} -n {ip}'.format(count=count, ip=ip_address),
                           shell = True,
                           stdout = subprocess.PIPE,
                           stderr = subprocess.PIPE)
    if reply.returncode == 0:
        return True, reply.stdout
    else:
        return False, reply.stdout + reply.stderr

def threads_ping(function, ip_address = '127.0.0.1', count = 3, limit = 1):
    with ProcessPoolExecutor(max_workers=limit) as executor:
        future = executor.submit(function, ip_address, count)
    return list(future.result())

if __name__ == '__main__':
    
    with open('check_ip_list', 'r') as chkList:
        for ip in chkList:
            all_done = threads_ping(ping_ip, ip, 3, 3)
            pprint(all_done)
