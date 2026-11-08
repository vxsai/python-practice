#final quest of L4 of CS50P

import sys
import statistics
import cowsay
import terrain

def main():
	if len(sys.argv) < 2 :
		sys.exit("Usage: python day10*3.py [alt1] [alt2] ...")

	raw_alts = sys.argv[1:]
	clean_alts = []
	
	for alts in raw_alts:
		try:
			clean_alts.append(float(alts))

		except ValueError :
			sys.exit(f"Error: '{alt}' is not a valid number.")

	base_y = statistics.mean(clean_alts)
	final_y = base_y + terrain.get_noise()

	cowsay.miki(f"Nyah! Spawning at Y-level {round(final_y, 1)}! Meow~")


main()
