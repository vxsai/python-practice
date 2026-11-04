#This quest combines multiple exceptions into a single workflow. In an automated pipeline, a user might ask for a material that doesn't exist, or they might type their requested quantity as a word instead of a number. You must catch both crashes independently.

def main():
	catalog = {"Sandstone":34 ,
		"Gravel":45 ,
		"Carrara":42 ,
		"Nero":12 ,
		"Deepslate":67 ,
		"Granite":67 
	}

	while True:
		try:
			material = input("Material: ").strip().title()
			quantity = int(input("Quantity: "))
			cost = quantity * catalog[material]
			print(f"Total cost: {cost}")

		except KeyError :
			print("Material not found.")

		except ValueError :
			print("Invalid quantity.")

		except EOFError :
			print()
			break

main()
