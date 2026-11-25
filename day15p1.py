#the persistent terminal logger (quest on L6)

def main():
	item = input("Log Item: ").strip().title()
	
	with open("vault15p1.txt", "a") as file:
		file.write(f"{item}\n")

	items = []
	with open("vault15p1.txt", "r") as file:
		for line in file:
			lines = line.rstrip()
			items.append(lines)

	print("---- Vault Contents ----")
	for saved in sorted(items):
		print(f"- {saved}")


if __name__ == "__main__":
	main()
