#L0-L3

def main():
	fleet = {"Alpha": 0, "Beta": 0, "Gamma": 0}
	while True:
		try:
			raw = input("Load (Truck, Weight): ")
			truck, w_str = raw.split(",")
			truck = truck.strip().title()
			weight = float(w_str.strip())
			current_load = fleet[truck]

			if weight <= 0:
				print("Error: Weight must be positive.")
			elif current_load + weight > 2000:
				print(f"Overload! {truck} cannot exceed 2000kg.")
			else:
				fleet[truck] += weight
				print(f"Loaded. {truck} is at {fleet[truck]}kg.")

		except KeyError:
			print("Unrecognized truck.")

		except ValueError:
			print("Invalid input. Format: Truck, Weight")

		except EOFError:
			print("\n--- FINAL DISPATCH MANIFEST ---")
			for t in fleet:
				print(f"{t}: {fleet[t]}kg")
			break

main()
