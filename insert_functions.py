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

def delete_user(id):
      conn.execute("DELETE FROM USERS \
            WHERE id = "+str(id))

      print(f"User with id {id} deleted")