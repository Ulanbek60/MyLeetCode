# first_number = int(input("Write the first number: "))
# second_number = int(input("Write the second number: "))
#
#
# number = 1
# while True:
#     if first_number != second_number:
#         s = first_number + number
#         s +=1
#     else:
#         break
#     print("Total: ", s)


# first_number = int(input("Write the first number: "))
# second_number = int(input("Write the second number: "))
#
# for i in range(first_number, second_number):
#     res = 0
#     res += i
#     s = res + i
#
#     print(s)

#
# digits = [1,2,3]
#
# new_list = []
# result_list = []
# for i in digits:
#     new_list.append(str(i))
#     res = str(int(''.join(new_list)) + 1)
# for d in res:
#     result_list.append(int(d))
#
# print(result_list)


# def lengthOfLastWord(s):
#     print(len(s.split()[-1]))
# lengthOfLastWord('Hello world')

# nums = [2,7,11,15]
# target = 9
# # a = dict(nums)
# new_list = []
# for i in range(len(nums)):
#     if target - i ==
#     print(i)

# twoSum([2,7,11,15])

#
# def minOperations(self, nums, k):
#     n = sum(nums)
#     count = 0
#     while True:
#         if n % k == 0:
#             return count
#         else:
#             n -= 1
#         count += 1
#

# def juice_machine(coins, price):
#     a = coins - price
#     if a % 3 == 0 :
#         print('Take your juice')
#     else:
#         print('Not enough change')
#
# juice_machine(10, 4)

#
# def juice_vitamin_score(fruits):
#     strawberry = 2
#     banana = 3
#     pineapple = 5
#     total_vitamins = 0
#     for i in fruits:
#         if i == strawberry:
#             total_vitamins += strawberry
#         elif i == banana:
#             total_vitamins += banana
#         elif i == pineapple:
#             total_vitamins += pineapple
#
#     if total_vitamins % 5 == 0:
#         print("Juice ready")
#     else:
#         print('Need more vitamins!')
#
#
# juice_vitamin_score(['banana'])

#
# aa = 'Hello World'
# a = 'd'
# print(a.join(aa))


# def change_word(mashina):
#     mashinaa = set(mashina)
#     a = str(mashinaa)
#     for i in a:
#         print(a.lower())
#
# change_word(['AUdi', 'TesLA', 'hONda', 'TEsLa'])
# # ('audi', 'tesla', 'honda')


#
# def climbStairs(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#
#     a = 1
#     b = 2
#
#     for i in range(3, n + 1):
#         temp = a + b
#         a = b
#         b = temp
#
#     print(b)
#
# climbStairs(6)
#
#
#
#
# def climbStairs3(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#
#     dp = [0] * (n + 1)
#     dp[0] = 1  # стоим на земле
#     dp[1] = 1  # только один способ: шаг на 1
#     dp[2] = 2  # [1+1], [2]
#
#     for i in range(3, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
#
#     return dp[n]


# def Coins(n):
#     dp = [0] * (n + 1)
#     dp[0] = 1
#
#     coins = [1, 2, 5]
#
#     for coin in coins:
#         for i in range(coin, n + 1):
#             dp[i] += dp[i - coin]
#     return dp[n]
#
# Coins(10)

































