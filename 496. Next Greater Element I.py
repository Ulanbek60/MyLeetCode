def nextGreaterElement(nums1, nums2):
    new_list = []
    for e in nums1:
        f = False
        p = nums2[nums2.index(e) + 1:]
        for k in p:
            if k > e:
                new_list.append(k)
                f = True
                break
        if not f:
            new_list.append(-1)
    return new_list

print(nextGreaterElement([4,1,2], [1,3,4,2]))


# 🗒️ Конспект: Что такое флаг
#
#     Флаг — это переменная (True/False), которая помогает помнить, произошло ли нужное событие.
#
#     Обычно начинается с False.
#
#     Если условие выполнено — ставим True.
#
#     Потом можно проверить флаг: если остался False — значит, ничего не произошло



a = [1, 3, 5, 1]
# b = [1, 3, 5, 7]

f = False
for i in a:
    if i % 2 == 0:
        f = True
        break

if f:
    print('YES')
else:
    print('NO')


