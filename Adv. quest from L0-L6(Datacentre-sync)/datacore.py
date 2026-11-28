# build an automated tool that reads a list of global server/factory sites from a CSV file, fetches live environmental telemetry from the Open-Meteo API (no API key required), calculates cooling risk, and exports a clean audit CSV.

def c_to_f(celsius):
	if celsius < -273.15:
		raise ValueError("Impossible temperature.")
	return round((celsius * 9 /5) + 32, 2)

def classify_cooling(celsius):
	if celsius >= 30.0 :
		return "HIGH COOLING"
	elif celsius >= 15.0 :
		return "NOMINAL"
	else:
		return "LOW COOLING"


def extract_temp(payload):
	return float(payload["current_weather"]["temperature"])

 
