# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curSum = 0


        def traverse(node):
            nonlocal curSum
            if not node:
                return
            
            traverse(node.right)
            temp = node.val
            node.val += curSum
            curSum += temp
            traverse(node.left)

        traverse(root)
        return root
