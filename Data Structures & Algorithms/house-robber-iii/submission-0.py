# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return [0,0]
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            withRoot = root.val + leftMax[1] + rightMax[1]
            withoutRoot = max(leftMax) + max(rightMax)
            return [withRoot, withoutRoot]
        return max(dfs(root))