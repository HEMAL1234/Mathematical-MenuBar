print("Main Menu:")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Quit")

def add():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another numner: "))
    print("Addition is: {}".format(num1 + num2))

def sub():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another numner: "))
    print("Substraction is: {}".format(num1 - num2))

def mul():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another numner: "))
    print("Multiplication is: {}".format(num1 * num2))

def div():
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another numner: "))
        print("Division is: {}".format(num1 / num2))
    except ZeroDivisionError as e:
        print(e)
while True:
    try:
        choice = int(input("Please make a choice: "))
    except:
        continue

    if choice == 1:
        add()
    if choice ==2:
        sub()
    if choice == 3:
        mul()
    if choice == 4:
        div()
    if choice == 5:
        break
