f = open('whitepages_1d61bd44c22ebb82370add59286e71d0.txt', 'r')

while True:
    x = f.read(1)
    if not x:
        break

    if ord(x) != 32:
        print("0", end="")
    else:
        print("1", end="")
