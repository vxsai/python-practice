#

def main():
	amount_due = 50
	while True:
		if amount_due <= 0:
			break

		print(f"amount due: {amount_due}" )
		coins = int(input("Insert coin: " ))

		if coins in [50 ,25 ,10 ,5 ]:
			amount_due -= coins

	print(f"Change owed: {abs(amount_due)}" )

main()
