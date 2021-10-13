import sqlite3

conn = sqlite3.connect('mhd.db')
print("Opened database successfully")


def read_users():
    cursor = conn.execute("SELECT * from USERS")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("PASSWORD = ", row[2], "\n")

    print("Read Users done successfully")


def read_protocoll():
    cursor = conn.execute("SELECT * from PROTOCOLL")
    for row in cursor:
        print("ID = ", row[0])
        print("CURRENTDATE = ", row[1])
        print("MHD = ", row[2])
        print("POINTS = ", row[3], "\n")

    print("Read Protocoll done successfully")


if __name__ == "__main__":
    read_users()
    read_protocoll()

    conn.close()
