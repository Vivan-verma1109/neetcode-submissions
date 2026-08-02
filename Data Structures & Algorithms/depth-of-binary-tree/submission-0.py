# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def find(root, depth):
            if not root:
                return depth - 1
            return(max(find(root.left, depth + 1), find(root.right, depth + 1)))       
        if not root:
            return 0
        return find(root, 1)
        