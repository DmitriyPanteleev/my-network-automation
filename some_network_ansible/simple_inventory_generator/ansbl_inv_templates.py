'''
Шаблон для переменных инвентори ансибла
'''

from jinja2 import Template

template_common_router = Template('''
---
ansible_ssh_host: {{ip_conn}}
ansible_ssh_user: device_admin
ansible_ssh_pass: super_password

''')

