
# Генератор переменных для инвентори ансибла из ip-плана.

import re
import csv
from ansbl_inv_templates import template_common_router

with open('ip-plan-vpn.csv', 'r', encoding='utf-8') as f_plan:
    reader = csv.reader(f_plan, delimiter = ";")
    for row in reader:
        point_name = 'other_entry'
        if row[8] == 'VPN офис':
            point_name = 'office_border_r'
        if row[8] == 'VPN НРКП':
            point_name = 'nrkp_border_r'
        with open(point_name + row[2], 'w') as f_var:
            f_var.write(template_common_router.render({'ip_conn':row[6]}))

# The End
