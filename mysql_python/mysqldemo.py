#!/bin/python3

import mysql.connector

db = mysql.connector.connect(
	host="localhost",
	user="<user_name_here>",
	password="<password_here>",
	db="<database_here>")

cur = db.cursor()

cur.execute("SELECT * FROM fruit")

for row in cur.fetchall():
	print(row)

db.close()

