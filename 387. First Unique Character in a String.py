s = "loveleetcode"
s = list(s)
for i, char in enumerate(s):
    if s.count(char) == 1:
        print(i)
        break
