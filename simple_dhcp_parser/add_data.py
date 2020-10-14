#!/usr/bin/env python

import sqlite3
import glob
import os
import re

def add_dhcpdb(db_filename, dhcp_snoop_files):

  db_exists = os.path.exists(db_filename)
  
  if db_exists:
    # Prepare DHCP date to insert   
    data_filename = 'dhcp_snooping.txt'
    regex1 = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    regex2 = re.compile('(sw\d+)')
    
    result_dhcp = []
    
    for dhcp_snoop_file in dhcp_snoop_files:
      
      with open(dhcp_snoop_file) as data:
        sw_name = regex2.search(dhcp_snoop_file)
        for line in data:
          match = regex1.search(line)
          if match:
            ext_match = list(match.groups())
            ext_match.append(list(sw_name.groups())[0])
            result_dhcp.append(tuple(ext_match))
    # Inserting data
    conn = sqlite3.connect(db_filename)

    print('Inserting DHCP Snooping data')
    for row in result_dhcp:
      try:
        with conn:
          query = '''insert into dhcp (mac, ip, vlan, interface, switch) values (?, ?, ?, ?, ?)'''
          conn.execute(query, row)
      except sqlite3.IntegrityError as e:
        print('Error occured: ', e)
    
    conn.close()
  else:
    print('Database does not exists. Please create it, before add date.')

def add_switchesdb(db_filename, switches_file):
  
  db_exists = os.path.exists(db_filename)
  
  if db_exists:
    # Prepare switches date to insert
    
    result_sw = []
    regex3 = re.compile('(sw\d+): ([A-Za-z0-9-, ]+)')

    with open(switches_file) as data:
      for line in data:
        match = regex3.search(line)
        if match:
          result_sw.append(match.groups())
    
    # Inserting data
    conn = sqlite3.connect(db_filename)
    
    print('Inserting Switch data')
    for row in result_sw:
      try:
        with conn:
          query = '''insert into switches (hostname, location) values (?, ?)'''
          conn.execute(query, row)
      except sqlite3.IntegrityError as e:
        print('Error occured: ', e)
    
    conn.close()
  else:
    print('Database does not exists. Please create it, before add date.')

if __name__ == '__main__':

  dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')

  add_switchesdb('dhcp_snooping.db', 'switches.yml')
  add_dhcpdb('dhcp_snooping.db', dhcp_snoop_files)
