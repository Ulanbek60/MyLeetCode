def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

print(count_vowels("hello world"))