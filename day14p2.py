#basic L5 quest of unit test on reactor quest

def check_core(temp):
	if temp > 1000 :
		raise ValueError("Core meltdown!")
	else:
		return "Stable."
