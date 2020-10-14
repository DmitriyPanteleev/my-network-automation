#!/usr/bin/env python

import os
import sqlite3

def create_dhcpdb(db_filename = 'dhcp_snooping.db', schema_filename = 'dhcp_snooping_schema.sql'):
  
  db_exists = os.path.exists(db_filename)
  
  if not db_exists:
    print('Creating schema...')
    conn = sqlite3.connect(db_filename)
    with open(schema_filename, 'r') as f:
      schema = f.read()
    conn.executescript(schema)
    conn.close()
    print('Done')    
  else:
    print('Database exists, assume dhcp table does, too.')

if __name__ == '__main__':

  create_dhcpdb()
