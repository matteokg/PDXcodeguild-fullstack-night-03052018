def fttom(x, y):
    #feet to meter
    if y == "ft":
        return x * 0.3048
def mitom(x,y):
    #Miles to meter
    if y == "mi":
        return x * 1609.34
def mtom(x,y):
    #Meter to meter
    if y == "m":
        return x * 1
def kmtom(x,y):
    #kilometer to meter
    if y == "km":
        return x / 1000

x = float(input("what is the distance").strip())
y = (input("what are the units? (ft, mi, m, km)")).lower().strip()

if y == "ft":
    print(fttom(x, y))
elif y == "mi":
    print(mitom(x,y))
elif y == "m":
    print(mtom(x,y))
elif y == "km":
    print(kmtom(x,y))

while True:
    again = input("Another operation? Yes/No").lower()
    if again == "yes" or again == "no"
        break
if again == "no"
    break
