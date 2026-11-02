#A petty wizard cursed the tavern so that vowels vanish from the air the moment someone speaks. You must write a script that continuously takes a traveler's sentences, strips out the vowels, and echoes the cursed result

def main():
	while True:
		speak = input("Speak: " ).strip()
		if speak.strip().title() == "Stop":
			break

		cursed = ""

		for char in speak:
			if char.lower() not in ["a", "e", "i", "o", "u" ]:
				cursed += char

		print(cursed)

main()
