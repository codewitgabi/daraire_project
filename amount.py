import sqlite3

connection = sqlite3.connect("foodly.db")
cursor = connection.cursor()

def view_balance(customer_email):
	cursor.execute("SELECT * FROM customer WHERE email=:email", {
		"email": customer_email
	})
	data = cursor.fetchone()
	
	if data == None:
		print ("No result found!")
	else :
		print(f"Your account balance is N{data[5]}")
	

def add_to_balance(customer_email):
	amount_to_deposit = int(input("ENTER AMOUNT YOU WISH TO DEPOSIT INTO YOUR ACCOUNT: "))
	
	cursor.execute("SELECT * FROM customer WHERE email=:email", {
		"email": customer_email
	})
	data = cursor.fetchone()
	
	if data != None:
		balance = data[5]
		balance += amount_to_deposit
		
		cursor.execute("""
		UPDATE customer
		SET balance=:balance
		WHERE email=:customer_email""", {"balance": balance, "customer_email": customer_email})
		connection.commit()
		print("Balance Updated!!")
		
	else :
		print ("Sorry you have no account with us")
