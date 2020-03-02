# Primera idea para partir desde algo.
#
# zsq*{t53z00w7124266z8et045t27q873220t}
# flag{...}


ciphertext = "abcdefghijklmnopqrstuvwxyz&%§$*/" # Todos los caracteres que existen en el texto. Leed el README para mas explicaciones, como, porque no hay mayusculas?
abc =        "axvdcfgpiqrszyojadleuvbutfiomngh" # Segun voy haciendo cambios, encuentro nuevas combinaciones, leed el README mejor.

f = open("ciphertext.txt", "r")
data = f.read()

answer = ""

for character in data:
    if character in ciphertext:
        pos = ciphertext.find(character)
        answer += abc[pos]
    else:
        answer += character

print(answer)
    
