# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class Solution:
#     def reverseList(self, head):
#         prev = None
#         curr = head
#         while curr:
#             next_node = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next_node
#         return prev
#
# # 👇 Создаём связанный список: 1 → 2 → 3 → None
# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
#
# n1.next = n2
# n2.next = n3
#
# # 👇 Вызываем решение
# sol = Solution()
# reversed_head = sol.reverseList(n1)
#
# # 👇 Печатаем результат
# while reversed_head:
#     print(reversed_head.val)
#     reversed_head = reversed_head.next




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

# 👇 Создаём связанный список: 1 → 2 → 3 → None
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(3)
n5 = ListNode(3)
n6 = ListNode(3)
n7 = ListNode(3)

n1.next = n2
n2.next = n3

# 👇 Вызываем решение
sol = Solution()
reversed_head = sol.reverseList(n1)

# 👇 Печатаем результат
while reversed_head:
    print(reversed_head.val)
    reversed_head = reversed_head.next
# print(reverseList(head = [1,2,3,4,5]))




