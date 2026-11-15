#will build a multi-file material synthesizer that takes a specific voxel material and a batch of temperature scans from the terminal, calculates the structural yield, handles corrupted data, and logs the averages.

import sys
import statistics
import cowsay
import forge13_1

def main():
	if len(sys.argv) < 3:
		sys.exit("Usage: python day13*1.py [ore] [heat1] [heat2].... ")

	ore = sys.argv[1].strip().title()
	heat_ini = sys.argv[2:]
	yield_log = []

	for heat in heat_ini:
		try: 
			heat = float(heat.strip())
		except ValueError:
			sys.exit(f"CRITICAL FALIURE: {heat} is not in valid format. Shutting Down")

		result = forge13_1.smelt(ore, heat)
		if result == 0.0:
			print("Ërror: Unknown material.")
			break

		yield_log.append(result)

		if result > 100:
			rating = "Ḧyper-Dense"
		elif result > 40:
			rating = "Stable"
		else:
			rating = "Fragile"

		print(f"Synthesized {ore} at {heat}C  ->  Yield: {result} [{rating}]")

	if len(yield_log) > 0:
		avg = round(statistics.mean(yield_log), 2)
		cowsay.trex(f"Average {ore.capitalize()} Yield; {avg}")

if __name__ == "__main__":
	main()
