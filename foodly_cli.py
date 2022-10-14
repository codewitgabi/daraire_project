import home
import menu
import amount


menu.create_table()
home.create_table()

exits = "YES"

print("*"*10 ,"WELCOME TO THE FOODLY APP", "*"*10)

print ("""
        SELECT AN OPTION BELOW:
        1) LOG IN
        2) CREATE AN ACCOUNT""")
        
request = int(input("ENTER A NUMBER: "))

if request == 1:
	customer_email = home.login()
	
	while exits == "YES" or exits == "Y":

		print ("""
		SELECT AN OPTION BELOW:
		1) TOP UP YOUR ACCOUNT BALANCE
		2) VIEW OUR MENU AND PRICING
		3) PLACE AN ORDER"""
		)
		
		answer = int(input ("ENTER A NUMBER: "))
	
		if answer == 2:
			menu.view_all_menu()
		elif request == 1:
			amount.add_to_balance(customer_email)
		else:
			print ("invalid input")
	
		exits = input ("DO YOU WISH TO CONTINUE: ").upper()


elif request == 2:
	home.add_names()
else:
	print ("invalid input")