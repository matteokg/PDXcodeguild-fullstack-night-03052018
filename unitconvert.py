def fttom(x, y):
    if y == "ft":
        return x * 0.3048
def mitom(x,y):
    if y == "mi":
        return x * 1609.34
def mtom(x,y):
    if y == "m":
        return x * 1
def kmtom(x,y):
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
