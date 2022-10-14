import sqlite3
from getpass import getpass

connection = sqlite3.connect("foodly.db")
cursor = connection.cursor()

def create_table():
	try:
		sql = """
		CREATE TABLE customer (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		firstname TEXT NOT NULL,
		lastname TEXT NOT NULL,
		email TEXT NOT NULL UNIQUE,
		password TEXT NOT NULL,
		balance INTEGER NOT NULL DEFAULT 0)
		"""
		cursor.execute(sql)
	except sqlite3.OperationalError:
		pass
		

def view_all():
	sql = "SELECT * FROM customer"
	for row in cursor.execute (sql):
		print (row)
		

def add_names():
	firstname = input("ENTER YOUR FIRSTNAME HERE: ")
	lastname = input("ENTER YOUR LASTNAME HERE: ")
	email = input("ENTER YOUR EMAIL HERE: ")
	pwrd = getpass("ENTER YOUR PASSWORD HERE: ")
	
	try:
		cursor.execute ("""
		INSERT INTO customer (firstname, lastname, email, password)
		VALUES (?,?,?,?)""",
		(firstname, lastname, email, pwrd))
		connection.commit()
		print ("added succesfully")
		
	except sqlite3.IntegrityError:
		print("Email Already in use!!!")
	

def login():
	email = input("Enter email to login: ")
	password = getpass("Password: ")
	
	data = cursor.execute("SELECT * FROM customer WHERE email=:email AND password=:password", {"email": email, "password": password})
	
	if data.fetchone() != None:
		return email
	else:
		print("Incorrect username or password")
		login()
	