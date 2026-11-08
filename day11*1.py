#custom library import quest~~~~~~~~

import sys
import statistics
import subprocess
import terrain

def main():
	if len(sys.argv) < 2:
		sys.stop("Usage: python spawn.py [alt1] [alt2] ...")

	raw_alts = sys.argv[1:]
	clean_alts = []

	for alts in raw_alts:
		try:
			clean_alts.append(float(alts))
		except ValueError:
			sys.exit(f"Error: '{alt}' is not a valid number.")

	base_y = statistics.mean(clean_alts)
	final_y = base_y + terrain.get_noise()

	# Call the compiled C graphics engine to render neko.png in high-res ASCII
	subprocess.run([
		"chafa", "-c", "full",
		 "-s", "140x140", "neko.png"

#————OR———

	#	"chafa", "-c", "full", "--fg-only",
        #       "--symbols", "ascii", "-s", "130x130", "neko.png"

	])

	print(f"\nNyah! Spawning at Y-level {round(final_y, 1)}! Meow~")

main()
