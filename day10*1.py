#importing library quest

import sys
import engine

def main():
	if len(sys.argv) != 3 :
		sys.exit("Usage: python game.py [Gravity] [Time]")

	try:
		g = float(sys.argv[1])
		t = float(sys.argv[2])

	except ValueError :
		sys.exit("Error: Gravity and Time must be numbers")

	v = engine.velocity(g,t)

	print(f"Velocity: {v}m/s.")

if __name__ == "__main__":
	main()
