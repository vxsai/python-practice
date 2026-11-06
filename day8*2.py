#L0-L3

def main():
	densities = {"Marble": 2700, "Granite": 2750, "Quartz": 2600}
	while True:
		try:
			raw_scan = input("Scan (Stone, Area, Thickness): ")
			stone, area_str, thick_str = raw_scan.split(",")
			stone = stone.strip().title()
			area = float(area_str.strip())
			thickness = float(thick_str.strip())
			density = densities[stone]
			weight = area * thickness * density

			if weight >= 1000 :
				print(f"Mass: {weight}kg. ROUTE TO CRANE.")

			else:
				print(f"Mass: {weight}kg. ROUTE TO FORKLIFT.")

		except ValueError :
			print("Error: Use format 'Stone, Area, Thickness' with numbers.")

		except KeyError :
			print("Error: Unrecognized material.")

		except EOFError :
			print("\nPowering down scanner...")
			break

main()
