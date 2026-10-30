#Python script that takes a traveler's order, calculates their total with the tax, and prints a formatted receipt.

name = input("Greetings sir,May i know your name? ").strip().title()

print(f"Welcome Mr.{name}")

def main():
    amount = float(input("How much money do you have sir? "))
    meal_cost = float(input("And cost of meal sir? "))

    cost = taxed_amount(meal_cost)

    print("————RECEIPT————")

    print("Sir your total with tax is=", round(cost , 2))

    print(f"So your remaining amount is= {amount-cost:.2f}")

def taxed_amount(meal_cost):
    return meal_cost*1.15

# as per 15% tax on meal

main()
