from flask import Flask, render_template, request, g, flash
import sqlite3
from flask_login import LoginManager, login_user

DATABASE = 'mhd.db'
login_manager = LoginManager()
app = Flask(__name__)
login_manager.init_app(app)
app.config.update(
    TESTING=True,
    SECRET_KEY='_5#y2L"F4Q8z'
)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def count_users():
      cursor = get_db().execute("SELECT MAX(ID) FROM USERS")
      for row in cursor:
            cu = row[0]
            if cu == None:
                  cu = 0
            return cu

@login_manager.user_loader
def load_user(user_id):
    return user_id

def insert_user(name, password):
      global users
      users = count_users()
      get_db().execute("INSERT INTO USERS (ID,NAME,PASSWORD) \
            VALUES ("+str(users+1)+", '"+name+"', '"+password+"')");

      get_db().commit()
      print(f"User {name} created")
      users += 1

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/create", methods=['POST', 'GET'])
def create():
	if request.method == "POST":
		if request.form['password'] ==  request.form['passwordrepeat']:
			try:
				insert_user(request.form['username'], request.form['password'])
			except:
				flash("Username taken")

	return render_template("Profil.html")

def check_password(name, password):
      cursor = get_db().execute("SELECT COUNT(1) FROM USERS \
            WHERE name = '"+name+"' \
            AND password = '"+password+"'")
      for row in cursor:
            return row[0]

@app.route("/login", methods=['POST', 'GET'])
def login():
	if request.method == "POST":
		if bool(check_password(request.form['username'], request.form['password'])):
			login_user()

	return render_template("Einloggen.html")


if __name__ == "__main__":
	app.run(debug=True)