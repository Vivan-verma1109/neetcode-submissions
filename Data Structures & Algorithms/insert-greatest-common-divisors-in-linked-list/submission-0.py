# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def gcd_iterative(a, b):
            a, b = max(a, b), min(a, b)
            while b != 0:
                a, b = b, a % b
            return a

        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head

        while head and head.next:
            temp = head
            second = head.next

            factor1 = temp.val
            factor2 = second.val

            insert = ListNode(gcd_iterative(factor1, factor2))
            temp.next = insert
            insert.next = second

            head = second

        return dummy.next
