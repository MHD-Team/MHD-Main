import sqlite3
conn = sqlite3.connect('mhd.db')

def insert_user(id, name, password):
      conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD) \
            VALUES ("+str(id)+", '"+name+"', '"+password+"')");

      conn.commit()
      print(f"User {name} created")


def insert_entry(id, currentdate, mhd, points):
      conn.execute("INSERT INTO PROTOCOLL (ID,CURRENTDATE,MHD,POINTS) \
            VALUES ("+str(id)+", '"+currentdate+"', '"+mhd+"', "+str(points)+")");

      conn.commit()
      print(f"Entry with id {id} created")

def delete_from_table(*tables):
      for table in tables:
            conn.execute(f"DELETE from {table};")
      print("Records from tables deleted successfully")

def delete_user(name):
      conn.execute("DELETE FROM USERS \
            WHERE name = '"+name+"'")

      print(f"User with id {id} deleted")

def check_password(name, password):
      cursor = conn.execute("SELECT COUNT(1) FROM USERS \
            WHERE name = '"+name+"' \
            AND password = '"+password+"'")
      for row in cursor:
            return row[0]

