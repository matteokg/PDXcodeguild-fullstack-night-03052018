import random

x=random.randint(1,10)

i=0
while i<10:
    guess = int(input("guess the number between 1 and 10?"))

    i= i+1


    if guess > x:
        print ("Too high, guess again")
    elif guess < x:
        print ("Too low, guess again")
    elif guess == x:
        break

if guess == x and i == 1:
    print("wow, you're a genius, it took 1 try. teach me your ways ")
elif guess == x and i>1:
    print("you win! it took you " + str(i) + ' ' + "tries. Why so many ya dingus?")
