import sqlite3
from insert_functions import *

conn = sqlite3.connect('mhd.db')
print("Opened database successfully")

delete_from_table("PROTOCOLL", "USERS")

insert_user("Paul", "123")
insert_user("Niklas", "456")

delete_user(1, "Paul")

insert_user("Lennart", "789")

insert_entry(2, '10.9.2021', '01.06.2021', 30)
insert_entry(4, '10.9.2021', '01.06.2021', 9)

conn.close()