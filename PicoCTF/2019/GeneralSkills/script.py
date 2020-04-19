f = open('lyrics.txt', 'r')
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
    x = f.read(1)
    if not x:
        break

    if x in abc:
        print(x, end = "")
