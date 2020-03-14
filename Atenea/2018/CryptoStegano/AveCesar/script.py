caesar = "Aquí iria el msg de la página de Atenea"

abc = "abcdefghijklmnopqrstuvwxyz"
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

solution = ""
jump = 0

asciiList = [ord(c) for c in caesar]
abc = [ord(c) for c in abc]
ABC = [ord(c) for c in ABC]

while(jump < 26):
    newList = []
    for c in asciiList:
        if(c in abc):
            c = ((c + jump) - 97) % 26 + 97
            newList.append(c)
        elif(c in ABC):
            c = ((c + jump) - 65) % 26 + 65
            newList.append(c)
        else:
            newList.append(c)

    newList = [chr(c) for c in newList]
    solution = "".join(newList)
    
    print(solution)
    jump += 1

