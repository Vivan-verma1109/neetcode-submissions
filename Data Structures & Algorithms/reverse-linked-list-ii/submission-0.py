# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        t = left - 1
        while t != 0:
            prev = prev.next
            t -= 1

        reversal = right - left + 1
        temp = prev.next
        connect = prev.next
        prevNode = None
        while reversal != 0:
            cur = temp.next
            temp.next = prevNode
            prevNode = temp
            temp = cur
            reversal -= 1
        prev.next = prevNode
        connect.next = temp
        return dummy.next