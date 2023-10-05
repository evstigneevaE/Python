n = float(input())
b = ''
o = ''
h = ''
hex_digits = "0123456789ABCDEF"
if n != int(n):
    print("Неверный ввод")
else:
    n = int(n)
    n1 = int(n)
    n2 = int(n)
    if n <= 0:
        print("Неверный ввод")
    else:
        while n > 0:
            b = str(n % 2) + b
            n = n // 2
        while n1 > 0:
            o = str(n1 % 8) + o
            n1 = n1 // 8
        while n2 > 0:
            h = hex_digits[n2 % 16] + h
            n2 = n2 // 16
print(b + "," + " " + o + "," + " " + h)



