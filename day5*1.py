#A blurry-eyed traveler is trying to settle their tab, but they keep handing you buttons, pocket lint, or slurring their words instead of giving you a solid number. You must build an input validator that refuses to crash.

def main():
	while True:
		try:
			amount = int(input("Write amount: "))
			break

		except ValueError :
			print("Please enter valid number. ")

	print(f"You paid {amount} amount. ")

main()
