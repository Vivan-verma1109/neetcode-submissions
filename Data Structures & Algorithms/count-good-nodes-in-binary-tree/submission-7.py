# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        def dfs(root, max_seen):
            nonlocal good
            if not root:
                return 
            
            if root.val >= max_seen:
                good += 1
            
            max_seen = max(max_seen, root.val)
            left = dfs(root.left, max_seen)
            right = dfs(root.right, max_seen)
        
        dfs(root, root.val)
        return good