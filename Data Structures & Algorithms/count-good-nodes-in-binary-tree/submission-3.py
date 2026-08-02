# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def traverse(root, max_seen):
            nonlocal count
            if not root:
                return
            
            if root.val >= max_seen:
                count += 1
                max_seen = max(root.val, max_seen)
            traverse(root.left, max_seen)
            traverse(root.right, max_seen)
        traverse(root, root.val)
        return count