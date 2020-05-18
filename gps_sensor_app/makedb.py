#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
from config import config

con = lite.connect(config['DB_NAME'])

with con:
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS sensor_data")
	cur.execute("""CREATE TABLE IF NOT EXISTS sensor_data (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		lat FLOAT,
		lon FLOAT, 
		gpstime VARCHAR(50), 
		systime VARCHAR(50), 
		alt FLOAT, 
		epv FLOAT, 
		ept FLOAT, 
		speed FLOAT, 
		climb FLOAT,
		macaddr VARCHAR(20),
		device_id VARCHAR(50)
		)""")
