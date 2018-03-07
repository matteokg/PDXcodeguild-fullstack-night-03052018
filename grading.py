score = int(input("What was the score?"))
plus_minus = ''
if score <= 94:
    print("A")
    print(plus_minus)
elif 80 <= score <= 90:
    print("B")
    print(plus_minus)
elif 70 <= score <= 80:
    print("C")
elif 60 <= score <= 70:
    print("D")
else:
    print("F")
