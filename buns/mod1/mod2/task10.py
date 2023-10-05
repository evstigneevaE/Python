s = input()
result = ''
for i in range(len(s)):
    if s[i] == ' ' and i!= 0:
        result += s[i-1]
result += s[i]
print(result)




