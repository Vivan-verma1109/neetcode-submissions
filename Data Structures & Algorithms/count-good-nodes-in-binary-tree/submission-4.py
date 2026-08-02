# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def seen(root, seen_max):
            nonlocal count
            if not root:
                return 
            if root.val >= seen_max:
                count += 1
                seen_max = max(seen_max, root.val)
            seen(root.left, seen_max)
            seen(root.right, seen_max)
        seen(root, root.val)
        return count