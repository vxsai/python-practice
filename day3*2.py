#A merchant just dropped off a wagon of supplies. You need to read the delivery manifest (a list) and update the tavern's master inventory (a dictionary) by adding the new items and increasing the counts of existing ones.

def main():
    inventory = {
        "Meat":23 ,
        "Bread":10 ,
        "Fish":17,
        "Cheese":13,
        "Ale":11
    }

    manifest = ["Bread", "Ale", "Cheese", "Ale", "Meat", "Bread", "Ale" ]

    for item in manifest:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    for item in inventory:
        print(f"{item}: {inventory[item]} " )

main()
