#cowsay library quest

import sys
import statistics
import cowsay

def main():
	if len(sys.argv) < 2 :
		sys.exit("Usage: python day10*2.py [fps1] [fps2] ...")

	scores = sys.argv[1:]
	fps_data = []

	for score in scores:
		try:
			fps_data.append(int(score))
		except ValueError :
			sys.exit(f"Error: '{score}' is not a valid number.")

	average_fps = statistics.mean(fps_data)
	cowsay.trex(f"Average FPS: {round(average_fps, 1)} FPS.")

main()
