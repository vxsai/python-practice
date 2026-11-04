#Workers at the loading dock are shouting out raw materials as they come off the truck. You need to log them continuously, count the duplicates, and print an alphabetized final manifest when the truck is empty (triggered by Ctrl-D).

def main():
	manifest = {}
	while True:
		try:
			material = input("Material: ").strip().upper()
			if material in manifest:
				manifest[material] += 1
			else:
				manifest[material] = 1

		except EOFError :
			print()
			break

	for item in sorted(manifest.keys()):
		print(f"{manifest[item]} {item}")

main()
