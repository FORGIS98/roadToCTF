cipher = "ndj'kt_qtvjc_ndjg_rgneid_psktcijgth" # uapv{ndj'kt_qtvjc_ndjg_rgneid_psktcijgth} = flag{...}

abc = "abcdefghijklmnopqrstuvwxyz"
newList = []
solution = ""
jump = 11

asciiList = [ord(c) for c in cipher]
abc = [ord(c) for c in abc]

for c in asciiList:
    if(c in abc):
        c = ((c + jump) - 97) % 26 + 97
    newList.append(c)

newList = [chr(c) for c in newList]
solution = "".join(newList)

print(solution)
