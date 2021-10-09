import sqlite3
from insert_functions import *
conn = sqlite3.connect('mhd.db')
delete_user(7, "Nic")