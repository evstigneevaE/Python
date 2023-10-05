a = input()
s = False
while 1:
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if i!=j:
                if a[i] == a[j] and a[i] != " ":
                    s = True
                    break
    break
print(s)


