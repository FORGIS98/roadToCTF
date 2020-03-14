flag = "aqui va el flag"
key = "aqui va la key"

solution = []

for c in range(len(flag)):
    solution.append(chr(ord(flag[c]) ^ ord(key[c])))

solution = "".join(solution)

print(solution)
