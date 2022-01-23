import sqlite3

conn = sqlite3.connect("mhd.db")


def insert_user(name, password):
    global users
    users = count_users()
    conn.execute(
        "INSERT INTO USERS (ID,NAME,PASSWORD)             VALUES ("
        + str(users + 1)
        + ", '"
        + name
        + "', '"
        + password
        + "')"
    )

    conn.commit()
    print(f"User {name} created")
    users += 1


def insert_entry(id, currentdate, mhd, points):
    conn.execute(
        "INSERT INTO PROTOCOLL (ID,CURRENTDATE,MHD,POINTS)             VALUES ("
        + str(id)
        + ", '"
        + currentdate
        + "', '"
        + mhd
        + "', "
        + str(points)
        + ")"
    )

    conn.commit()
    print(f"Entry with id {id} created")


def delete_from_table(*tables):
    for table in tables:
        conn.execute(f"DELETE from {table};")
    print("Records from tables deleted successfully")


def delete_user(id, name):
    conn.execute(
        "DELETE FROM USERS             WHERE name = '"
        + name
        + "'             AND id = "
        + str(id)
    )

    print(f"User {name} deleted")
    # users -= 1


def check_password(name, password):
    cursor = conn.execute(
        "SELECT COUNT(1) FROM USERS             WHERE name = '"
        + name
        + "'             AND password = '"
        + password
        + "'"
    )
    for row in cursor:
        return row[0]


def total_points(id):
    cursor = conn.execute(
        "SELECT SUM(Points) FROM Protocoll                   WHERE id = " + str(id)
    )

    for row in cursor:
        total = row[0]
        if total is None:
            total = 0

        return total


def count_users():
    cursor = conn.execute("SELECT MAX(ID) FROM USERS")
    for row in cursor:
        cu = row[0]
        if cu is None:
            cu = 0
        return cu
    return 0
