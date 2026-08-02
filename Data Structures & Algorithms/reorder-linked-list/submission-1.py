# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        h2 = slow.next
        slow.next = None

        #reverse h2
        temp = h2
        prev = None
        while temp:
            cur = temp.next
            temp.next = prev
            prev = temp
            temp = cur
        h2 = prev

        first, second = head, h2
        while second:
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first, second = nxt1, nxt2
