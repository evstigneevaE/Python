a = int(input())
for i in range(1, a+1):
    for j in range(1, a+1):
        if j != a:
            print(j, end=', ')
        else:
            print(j)
print()
for i in range(1, a+1):
    for j in range(1, a+1):
        if j != a:
            print(i, end=', ')
        else:
            print(i)

