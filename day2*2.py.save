#The Scenario
#Your ledger is working perfectly, but now the tavern needs an automated bouncer. Your script must evaluate a traveler's race, party size, and wallet to assign them the correct seating using logical control flow.


def main():
    race = input("what's your race? ").strip().title()

    match race:
        case "Dwarf":
            print("Ah, i see so you're an dwarf! ")
        case "Orc":
            print("Ohh.. orc! Sir keep your temper in check  ")
        case "Elf":
            print("Welcome elf! have some booze ")
        case _:
            print("Welcome sir! ")


    members = int(input("what's your party size? "))

    if is_even(members):
        print("You get a square table. ")
    else:
        print("You got round table. ")


    coins = int(input("How much silver coins do you have? "))

    if coins >= 50 and members <= 4:
        print("You got VIP lounge. ")
    elif coins < 10 or race == "Orc":
        print("The stables. ")
    else:
        print("Go to main dinning room. ")

def is_even(members):
    return members % 2 == 0

main()
