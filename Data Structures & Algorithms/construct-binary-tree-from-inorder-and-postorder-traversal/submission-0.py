# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def build(inorder, postorder):
            if not inorder or not postorder:
                return
            
            root = postorder[-1]

            mid = inorder.index(root)

            left = inorder[:mid]
            right = inorder[mid + 1:]

            postorder_left = postorder[:len(left)]
            postorder_right = postorder[len(left): -1]

            return TreeNode(root, build(left, postorder_left), build(right, postorder_right))

        return build(inorder, postorder)