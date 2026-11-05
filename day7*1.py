#You are calculating live quotes for clients at the marble yard. You need to ask for a stone type, ask for the area in square meters, apply a discount for massive bulk orders, and keep a running total of their entire bill until they are done ordering (Ctrl-D).

def main():
	catalog = {"Sandstone":83 ,
		"Blackstone":57 ,
		"Nero":78 ,
		"Marble":98 ,
		"Granite":120 ,
	}

	total_bill = 0.0
	while True:
		try:
			stone = input("Stone: ").strip().title()
			price = catalog[stone]
			area = int(input("Square Meters: "))

			if area >= 10 :
				cost = (price*area)*0.9
			else:
				cost  = price*area

			total_bill += cost
			print(f"Total bill: ${total_bill}")
		except (KeyError , ValueError) :
			pass

		except EOFError :
			print(f"\nTotal: ${total_bill}")
			break

main()
