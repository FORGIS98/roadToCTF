import string

abc = string.ascii_uppercase
txt = [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]

answ = ""
for x in txt:
    answ += abc[x - 1]

print(answ)
