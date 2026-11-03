#The bartender checks the main ale keg and writes down its remaining volume as a fraction (like "3/4"). You need to convert that fraction into a percentage. If they write gibberish, or claim the keg has a capacity of zero, the program must reject it without crashing.

def main():
	while True:
		try:
			x_str , y_str = input("Keg fraction: ").split("/")
			x = int(x_str)
			y = int(y_str)

			if x > y :
				continue

			percentage = round((x/y) * 100)
			break

		except ValueError :
			pass

		except ZeroDivisionError :
			pass

	if percentage <= 1:
		print("Empty ")

	elif percentage >= 99:
		print("Full ")

	else:
		print(f"{percentage}%")

main()
