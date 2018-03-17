import random

winnings = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}

def pick6():
    numbers = []

    for i in range(6):
        numbers.append(random.randint(1, 99))
    return numbers


def number_matches(winning, ticket):
    match = 0

    for i in range(len(winning)):
        if winning [i]==ticket[i]:
            match += 1
    return match




if __name__ == '__main__':
    winner = pick6()
    balance = 0
    earnings = 0

    for i in range(1000000):
        ticket = pick6()
        balance -= 2
        matches = number_matches(winner, ticket)
        balance += winnings[number_matches(winner, ticket)]


    print(f"your final balance is: {balance}")
    print(f"your roi was: ")
