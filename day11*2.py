#will build a chunk generator that takes a layer count from the command line, loops through each layer, calculates physical density using a custom module, and assigns a biome using logic gates.

import sys
import random
import chunk11_2
import cowsay

def main():
	if len(sys.argv) != 2 :
		sys.exit("Usage: python day11*2.py [layers]")

	try:
		layers = int(sys.argv[1])
	except ValueError:
		sys.exit("Error: Number of layers must be integers.")
	
	for depth in range(1 , layers + 1):
		temp = random.randint(-50,90) 
		if temp < 0:
			biome = "Glacial Ice"
		elif temp <= 45:
			biome = "Temperate Stone"
		else:
			biome = "Volcanic Magma"

		density = chunk11_2.calc_density(depth)

		print(f"Layer {depth} | Biome: {biome} | Temp: {temp}C | Density: {density} kg/m3")

	cowsay.dragon("Chunk generation completed!")

if __name__ == "__main__":
	main()
