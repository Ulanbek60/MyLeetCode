def uncommonFromSentences(s1, s2):
    new_list = []

    return list(set(s1.split()) ^ set(s2.split()))
# print(uncommonFromSentences('this apple is sweet', 'this apple is sour'))

s1 = "d b zu d t"
s2 = "udb zu ap"
c = [i for i in set(s1.split() + s2.split()) if str(s1 + ' ' + s2).count(i) == 1]
print(c)


# керектуулорун алып жаныга салып пайда кыл