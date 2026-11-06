#L0-L3

def main():
	prices = {"Marble": 120, "Granite": 90, "Quartz": 85}
	while True:
		try:
			raw_msg = input("WhatsApp: ")
			client, stone, qty_str = raw_msg.split(",")
			client = client.strip().title()
			stone = stone.strip().title()
			qty = int(qty_str)
			base_cost = prices[stone] * qty
			
			if base_cost >= 1000 :
				shipping = 0
			else:
				shipping = 150

			print(f"Invoice for {client}: ${base_cost + shipping} (Includes ${shipping} shipping)")

		except ValueError :
			print("Error: Format must be 'Name, Stone, Qty'.")

		except KeyError :
			print("Error: Stone not found in catalog.")

		except EOFError :
			print("\nDisconnecting WhatsApp server...")
			break

main()
