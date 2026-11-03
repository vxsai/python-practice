#An ogre has walked into the tavern and will keep ordering food until he passes out. You must take his order continuously, ignoring items you don't sell, until the user forces the program to stop by pressing Ctrl-D (which simulates an End-Of-File or EOFError).

def main():
	menu = {"Beaf":25 ,
		"Bread":33,
		"Pie":11,
		"Ramen":45,
		"Booze":67
	 }

	total = 0
	while True:
		try:
			item = input("Food name: ").strip().title()
			total += menu[item]
			print(f"Total: {total}")

		except KeyError :
			pass

		except EOFError :
			print()
			break

main()
