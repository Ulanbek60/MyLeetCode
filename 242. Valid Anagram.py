def isAnagram(s, t):
    s_list = sorted(list(s))
    t_list = sorted(list(t))

    return s_list == t_list
print(isAnagram("anagram", "nagaram"))