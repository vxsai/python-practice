import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python day9*4.py [USD_Amount]")
        
    try:
        usd = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Amount must be a number.")
        
    response = requests.get("https://open.er-api.com/v6/latest/USD")
    data = response.json()
    rates = data["rates"]
    
    print(f"\n———CONVERTING ${usd} USD TO ALL CURRENCIES———")

    for currency, rate in rates.items():
        total = usd*rate
        print(f"{currency}: {round(total, 2)}")

main()

