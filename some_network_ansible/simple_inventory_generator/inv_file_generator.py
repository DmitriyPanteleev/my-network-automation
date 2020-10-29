
# Генератор инвентори файла.

import os

inv_list = os.listdir('./host_vars/')

print(inv_list)

with open('uskfo_hosts_ag', 'w') as inv_file:
    for host in inv_list:
        inv_file.write(host+'\n')

# The End
