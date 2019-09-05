""" 

The basic structure of program :

def some_function(some_argument):

  # do stuff and or do not return data

def another_function():

  # do other stuff and return data

def start_my_program():

  # all of your code from assignment 5, be sure to indent!

  # at some point call the functions defined above

start_my_program()"""
def beginn_msg():	
	print("Welcome to our \"Family Kitchen\"!!! It\'s new restaurant in town.")
	
def choose():
	start_msg = ("Do you wanna see our daily menu? (Y/N):")
	start_answer =input(start_msg)
	return start_answer		
	
def menu():
	breakfast={"2.50$":"BREAKFAST PIE",
		   "5.74$":"TOAST",
		   "3.25$":"EGGS, HASHBROWNS & TOAST",
		   "2.20$":"PANCAKE",
		   "3.25$":"CROISSANT FRENCH TOAST",
		   "5.25$":"KLUB SANDWICH"
		   }
	lunch={	"12.52$":"MEATLOAF PLATE",
		"14.32$":"FRIED CHICKEN PLATE",
		"18.24$":"HOT TURKEY PLATE",
		"11.00$":"POT ROAST",
		"21.74$":"FISH & CHIPS",
		"14.26$":"ALL AMERICAN BURGER"
			}
	dinner={"9.28$":"GRILLED PORK CHOP",
		"16.27$":"COUNTRY FRIED SHRIMP",
		"9.24$":"HAMBURGER STEAK",
		"14.82$":"ROAST BEEF",
		"12.79$":"FRIED CHICKEN LIVERS",
		"8.12$":"COUNTRY HAM WITH VEGETABLES"

			}
	snack={"2.52$":"FROZEN YOGURT",
	   "2.52$":"ICECREAM",
	   "4.38$":"CUP OF FRUITS",
	   "1.98$":"MUFFINS"

	}
	menu = ["breakfast", "lunch", "dinner", "snack"]
	print ("Today we offer:")
	for i, j in enumerate(menu):
		print (i + 1, '-', j)
	user_input = input("Please type number 1-4 to see our daily menu: ")
	if user_input == "1":
		for b in breakfast:
			print (b,breakfast[b])
	elif user_input == "2":
		for l in lunch:
			print (l,lunch[l])
	elif user_input == "3":
		for d in dinner:
			print (d,dinner[d])
	elif user_input == "4":
		for s in snack:
			print (s,snack[s])
	else:
		print("You haven\'t put right number.Please choose between 1-4")
		
def start_again ():
	restart_msg = ("If you want see our daily menu again press(y/n):")
	restart_answer =input(restart_msg)
	return restart_answer

def start_my_program ():
	beginn_msg()
	a = choose()
	if a == "Y" or a == "y":
		menu()
		y = start_again()
		if y == "y" or y == "Y":
			return start_my_program()
		else:
			print ("Thank you! See you next time")	
	elif a == "n" or a == "N":
		print ("Thank you! See you next time")
	else:
		print ("Wrong input.Please try again!")
		return start_my_program()			
		

if __name__ == "__main__":
    start_my_program()
