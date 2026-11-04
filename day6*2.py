#Final concpet of CS50P L3

def get_measurement(prompt):
	while True:
		try:
			return int(input(prompt))

		except ValueError :
			pass

def main():
	lenght = get_measurement("Slab lenght (cm): ")
	print(f"Recorded lenght: {lenght} cm ")

main()
