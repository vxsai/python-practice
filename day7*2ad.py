#advance quest for basics from L0-L3

def main():
	inventory = {"Granite": [90, 50],
		 "Quartz": [85, 20],
		"Blackstone":[75,15],
		"Nero":[57,23]
	}
	total = 0

	while True:
		try:
			item_str, qty_str = input("Order (Item, Qty): ").split(",")
			item = item_str.strip().title()
			qty = int(qty_str.strip())
			stock = inventory[item][1]

			if qty <= inventory[item][1]:
				inventory[item][1] -= qty
				total += (inventory[item][0]*qty)
				print(f"Processed: {qty} {item}")

			else:
				 print(f"Insufficient stock. Only {stock} left.")

		except KeyError :
			print("Item not found")

		except ValueError :
			print("Invalid. Use: item , qty")

		except EOFError :
			print(f"\n\nTotal revenue: ${total}")
			print("Remaining Stock: ")
			for material in inventory:
				print(f"{material}: {inventory[material][1]}")
			break

main()
