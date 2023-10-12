s = input().split()
print(True if [True for i in range (len(s)) if s[i-1] == s[i]] else False)

