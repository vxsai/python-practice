# CS50P L4 quest

import sys
import statistics
import cowsay
import raymath12_1

def main():
	if len(sys.argv) < 2 :
		sys.exit("Prompt: python day12*1.py [distance]")
	raw_distance = sys.argv[1:]
	
	for distance in raw_distance :
		try:
			dist = float(distance)
		except ValueError:
			print(f"Skipping invalid data: {distance}")
			continue

		if dist < 5:
			material = "Obsidian"
		elif dist <=15:
			material = "Water"
		else:
			material = "Air"

		light = raymath12_1.calc_light(dist)

		print(f"Ray hit {material} at {dist}m | Light Intensity: {light}%")

	cowsay.trex("Render cycle complete!")

if __name__ == "__main__":
	main()
