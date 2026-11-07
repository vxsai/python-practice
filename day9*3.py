#library importing quest

import sys
import requests

def main():
	if len(sys.argv) != 2:
		sys.exit("Usage: python day9*3.py [USD_Amount]")

	try:
		usd = float(sys.argv[1])
	except ValueError :
		sys.exit("Error: Amount must be a number.")


	# Fetching live data from the API
	response = requests.get("https://open.er-api.com/v6/latest/USD")
	data = response.json()
	inr_rate = data["rates"]["INR"]
	total_inr = usd * inr_rate

	print(f"Export Invoice: ${usd} USD = ₹{round(total_inr, 2)} INR")


main()
