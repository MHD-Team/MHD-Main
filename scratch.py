import sqlite3
conn = sqlite3.connect('mhd.db')
conn.execute("""DROP TABLE USERS""")