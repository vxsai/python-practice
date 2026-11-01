#The traveler made it past the bouncer and is ready to order drinks. You need to write a script that continuously takes their order until they are finished, stores their items, and calculates the final tab

def main():
    menu = {"Ale": 15, "Mead": 13, "Roast": 21, "Fronche": 17}
    order = []
    
    while True:
        item = input("Item: ").strip().title()
        if item == "Done" :
            break

        if item in menu:
            order.append(item)

        else:
            print("We don't serve it here. ")


    total = 0
    for item in order:
        total = menu[item] + 1

    print(f"You have order {len(order)} items. Your total tab is {total} silver")

main()
        
