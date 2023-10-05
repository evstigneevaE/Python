start = time.time()
line = input()
count_1 = 0
count_0 = 0
for i in line:
    if i == '1':
        count_1 += 1
    else:
        count_0 += 1
if count_1 == count_0:
    print('yes')
else:
    print('no')
