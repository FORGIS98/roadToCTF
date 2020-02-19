# This is our first hypothesis:
#
# izu rpjm ky "izux jpp pksue zjhhkpx uoug jriug".
# the flag is "..."


ciphertext = "abcdefghijklmnopqrstuvwxyz" # This is what we have in the ciphertext
abc =        "uxzcdorptailgbvljfvmewnysh" # This is what I change letter by letter every time I run the script and find new words (read README file to better understand)

f = open("ciphertext.txt", "r")
data = f.read()

answer = ""

for line in data:
    if line in ciphertext:
        answer += abc[ord(line) - 97]
    else:
        answer += line

print(answer)
    
