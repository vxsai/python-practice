#quest on csv importing

import csv

def main():
	mat = input("Material: ").strip().title()
	dens = float(input("Density: ").strip())

	with open("day15p2.csv", "a", newline="") as file:
		writer = csv.DictWriter(file, fieldnames=["name", "density"])
		writer.writerow({"name": mat, "density": dens})

	with open("day15p2.csv", "r") as file:
		reader = csv.DictReader(file)
		for row in reader:
			print(f"- {row['name']}: {row['density']} g/cm3")


if __name__ == "__main__":
	main()
