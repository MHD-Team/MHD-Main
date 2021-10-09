import sqlite3

def create_users():
	conn = sqlite3.connect('mhd.db')

	print("Opened database successfully")

	conn.execute("""CREATE TABLE IF NOT EXISTS USERS
	         (ID INT PRIMARY KEY     NOT NULL,
	         NAME TEXT   UNIQUE NOT NULL,
	         PASSWORD       TEXT    NOT NULL);""")
	print("Table Users created successfully")

	conn.close()



def create_protocoll():
	conn = sqlite3.connect('mhd.db')

	print("Opened database successfully")

	conn.execute("""CREATE TABLE IF NOT EXISTS PROTOCOLL
	         (ID             INT     NOT NULL,
	         CURRENTDATE     DATE    NOT NULL,
	         MHD             DATE    NOT NULL,
	         POINTS          INT     NOT NULL);""")
	print("Table protocoll created successfully")

	conn.close()


if __name__ == "__main__":
	create_users()
	create_protocoll()