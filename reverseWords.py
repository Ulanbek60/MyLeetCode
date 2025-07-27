s = "Let's take LeetCode contest"

nl = []
reversed_word = s.split()
for i in reversed_word:
    nl.append(i[::-1])
print(' '.join(nl))