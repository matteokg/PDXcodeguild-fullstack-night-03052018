def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

while True:
    print("What operation would you like to perform?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose 1/2/3/4")

    num1 = int(input("First number").strip())
    num2 = int(input("Second number").strip())

    if choice == "1":
        print (num1, '+', num2, '=', add(num1, num2))
    elif choice == "2":
        print (num1, '-', num2, '=', subtract(num1, num2))
    elif choice == "3":
        print (num1, 'x', num2, '=', multiply(num1, num2))
    elif choice == "4":
        print (num1, '/', num2, '=', divide(num1, num2))


    again = input("Another operation? Yes/No").lower().strip()
    if again == "yes":
        continue
    elif again == "no":
        break
