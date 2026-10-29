name = input("what's your name? ").strip().title()
print("Hello,", name)


#simple decimal additon
x = float(input("write value of x="))
y = float(input("write value of y="))

print(f"{x+y:.3f}")

#or print(round(a + b, 3))

#most important one (creatinf own fxn) 

def main():
    a = float(input("write value of a="))
    b = float(input("write value of b="))

    result = add(a,b)

    print(round(result, 3))

def add(a,b):
    return a + b

main()
