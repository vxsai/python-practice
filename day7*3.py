#Automated saw quest

def main():
	process(240)
	process(300)


def process(total_length):
	while True:
		try:
			cut = int(input(f"Cutting {total_length}cm board. Cut size: "))
			pieces = total_length // cut
			
		except ValueError :
			print("Invalid input. Numbers only")

		except ZeroDivisionError :
			print("Saw can't make 0cm cuts.")

		else:
			scrap = total_length % cut
			print(f"Yield: {pieces} pieces. Scrap: {scrap}cm")
			return

main()
