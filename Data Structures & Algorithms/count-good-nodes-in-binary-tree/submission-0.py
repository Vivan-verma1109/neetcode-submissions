# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root, max_seen):
            nonlocal count

            if not root:
                return None

            if root.val >= max_seen:
                count += 1
            max_seen = max(max_seen, root.val)
            dfs(root.left, max_seen)
            dfs(root.right, max_seen)
        dfs(root, root.val)
        return (count)