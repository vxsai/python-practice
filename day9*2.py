#argv quest

import sys

def main():
	if len(sys.argv) < 3:
		sys.exit("Error: Too few arguments. Use: python file.py [Stone] [Qty]")

	elif len(sys.argv) > 3:
		sys.exit("Error: Too many arguments.")

	try:
		stone = sys.argv[1].strip().title()
		qty = int(sys.argv[2])
		print(f"Express Dispatch: {qty} units of {stone} routed for delivery.")

	except ValueError :
		sys.exit("Error: Quantity must be a whole number.")

main()
