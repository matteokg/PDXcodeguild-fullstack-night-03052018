import random


char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*"


password = ''

for i in range(10):
    password += random.choice(char)
    i = i + 1

print(password)
