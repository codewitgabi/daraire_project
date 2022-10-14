import sqlite3

connection = sqlite3.connect("foodly.db")

cursor = connection.cursor()

def create_table():
	try:
		sql = '''
		CREATE TABLE menu (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		menu TEXT NOT NULL,
		price INTEGER NOT NULL DEFAULT 0)
		'''
		cursor.execute(sql)
	except sqlite3.OperationalError:
		pass


def view_all_menu():
	print("=" * 40)
	print("*" * 10, "Foodly Menu", "*" * 10)
	print("=" * 40)
	
	print("Menu".rjust(8), "Price".rjust(25))
	
	sql = "SELECT menu, price FROM menu"
	
	for row in cursor.execute(sql):
		print(row[0], row[1])


def add_menu():
	menu = input("ENTER YOUR FOOD MENU HERE: ")
	price = int(input("ENTER THE PRICE HERE: "))
	
	cursor.execute ("INSERT INTO menu (menu, price) VALUES (?, ?)", (menu, price))
	connection.commit()
	print ("added succesfully")
	