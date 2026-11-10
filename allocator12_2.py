#library for day12*2 quest

import random

def calc_stress(voxels,ram):
	x = random.uniform(0.8,1.2)
	return round((x*voxels)/ram ,2)
