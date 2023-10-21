list = input().split()
if len(list) == len(set(list)):
    print('Все числа разные')
elif len(set(list)) == 1:
    print('Все числа равны')
else:
    print('Есть равные и неравные числа')