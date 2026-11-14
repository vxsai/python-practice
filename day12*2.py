#will build a memory allocator module and a main profiler that tests multiple voxel chunks at once.

import sys
import statistics
import cowsay
import allocator12_2

def main():
	if len(sys.argv) < 3:
		sys.exit("Usage: python day12*2.py [ram_mb] [chunk1] [chunk2] ...")

	alerts = {"OPTIMAL": "Stable", "HEAVY": "Warning", "CRITICAL": "Overload"}

	ram_input = sys.argv[1]
	chunks = sys.argv[2:]
	stress_log = []

	for chunks in chunks:
		try:
			ram = int(ram_input)
			voxels = int(chunks)
			stress = allocator12_2.calc_stress(voxels, ram)
		except ValueError:
			print(f"Error: Skipping corrupted chunk {chunks}")
			continue
		except ZeroDivisionError :
			sys.exit("Crash: 0 MB RAM allocated!")
		
		stress_log.append(stress)

		if  stress < 10:
			state = "OPTIMAL"
		elif stress <= 25:
			state = "HEAVY"
		else:
			state = "CRITICAL"

		print(f"Chunk: {voxels} voxels -> Stress: {stress} [{state} — {alerts[state]}]")

	avg = round(statistics.mean(stress_log),2)
	cowsay.tux(f"Average Engine Stress: {avg}")

if __name__ == "__main__":
	main()
