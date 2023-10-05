s = input()
glasnya = "аеёиоуыэюя"
count1 = 0
count2 = 0
for i in s:
    if i in glasnya:
        count1 += 1
    else:
        count2 += 1
print(count1)