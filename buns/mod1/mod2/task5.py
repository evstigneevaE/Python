a = input()
alph = 'abcdefghijklmnopqrstuvwxyz'
i = a[:1]
n = int(a[2:])
index = 0
for j in range(len(alph)):
    if alph[j] == i:
        index = j
result = (index + n) % 26
print(alph[result])