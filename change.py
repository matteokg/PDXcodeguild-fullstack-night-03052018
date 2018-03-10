while True:
    change = float(input("Please enter an amount"))
    change = change * 100
    print(int(change//25), "quarters")
    change = change%25
    print(int(change//10), "dimes")
    change = change%10
    print(int(change//5), "nickels")
    change = change%5
    print(int(change//1), "pennies")

    again = input("Another amount?").strip().lower()
    if again == "yes":
        continue
    elif again == "no":
        break
