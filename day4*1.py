#A rowdy dwarf is throwing darts in the tavern. You need to record an unknown number of throws, then review the final sequence to count his bullseyes.

def main():
	throws = []

	while True:
		score = input("What's the score? " ).strip().title()

		if score == "Done":
			break

		throws.append(int(score))

	bullseyes = 0
	for score in throws:
		if score == 50:
			bulleseyes = bullseyes + 1

	print(f"Dwarf threw {len(throws)} and hit {bullseyes} bullseyes! ")

main()
