s = input()
ind = s.find(",")
a = s[:ind]
b = s[ind+1:]
count = 0
while 1:
    s = a[0]
    if s != b:
        count += 1
        a = a[1::]
    else:
        count += 1
        print(count)
        break

