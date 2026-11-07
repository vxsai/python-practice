#quest on library

import random

def main():
	batch = ["Carrara", "Granite", "Quartz", "Onyx"]

	while True:

		try:
			input("Press Enter to test next slab...")
			stone = random.choice(batch)
			score = random.randint(1,100)
	
			if score >= 50 :
				print(f"{stone} passed QA with {score} PSI.")

			else:
				print(f"{stone} SHATTERED at {score} PSI.")

		except EOFError :
			print("\nShutting down QA machine.")
			break

main()
