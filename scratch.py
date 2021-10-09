import sqlite3
from insert_functions import *
conn = sqlite3.connect('mhd.db')
cursor = conn.execute("SELECT SUM(Points), 0 FROM Protocoll \
            WHERE id = 1")


for row in cursor:
	print(row)