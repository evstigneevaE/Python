a = input()
f = ''
while 1:
    if len(a) > 0:
        st = a[0]
        if st!= '.':
            f += st
            a = a[1::]
        else:
            print(f)
            a = a[1::]
            otv = ''
    else:
        print(f)
        break