# This is our first hypothesis:
#
# izu rpjm ky "flag".
# the flag is "..."


ciphertext = "abcdefghijklmnopqrstuvwxyz" # Letras del cifrado
abc =        "uxzcdorptailgbvljfvmewnysh" # Letras que cambio poco a poco.

f = open("ciphertext.txt", "r")
data = f.read()

answer = ""

for line in data:
    if line in ciphertext:
        answer += abc[ord(line) - 97]
    else:
        answer += line

print(answer)
    
