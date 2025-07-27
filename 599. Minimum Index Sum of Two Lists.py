def findRestaurant(list1, list2):
    index_map = {word: i for i, word in enumerate(list1)}
    min_sum = float('inf')
    result = []

    for j, word in enumerate(list2):
        if word in index_map:
            total = j + index_map[word]
            if total < min_sum:
                min_sum = total
                result = [word]
            elif total == min_sum:
                result.append(word)

    return result
print(findRestaurant(["Shogun", "KFC", "Burger King"], ["KFC", "Shogun", "Burger King"]))
