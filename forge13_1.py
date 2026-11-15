#custom library for quest day13*1

import random

def smelt(ore, heat):
	base_yields = {"Obsidian": 4.5,
		"Quartz": 2.1,
		"Carbon": 1.8
	}

	if ore not in base_yields:
		return 0.0

	final_yield = base_yields[ore]*heat*random.uniform(0.8,1.2)
	return round(final_yield, 2)
