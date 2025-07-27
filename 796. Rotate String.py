def rotateString(s, goal):
    if len(s) != len(goal):
        print(False)
    for i in range(0, len(s)):
        if s == goal:
            print(True)
        s = s[:1] + s[0]
    print(False)

print(rotateString('abcde', 'cdeab'))