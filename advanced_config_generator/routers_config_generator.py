#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import os

# Howto use: routers_config_generator.py templates/for.txt data_files/for.yml
TEMPLATE_DIR, template = os.path.split(sys.argv[1])
VARS_FILE = sys.argv[2]

env = Environment(
    loader=FileSystemLoader(TEMPLATE_DIR),
    trim_blocks=True,
    lstrip_blocks=True)
template = env.get_template(template_file)

vars_dict = yaml.load(open(VARS_FILE))
routers = yaml.load(open('routers_data.yml'))

for router in routers:
    r1_conf = router['name'] + '_r1.txt'
    with open(r1_conf, 'w') as f:
        f.write(template.render(vars_dict))
