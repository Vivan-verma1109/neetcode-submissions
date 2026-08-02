# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder root left right
        # innorder left root right
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        # i gotta find where that is in innorder
        s = {}
        for i, idx in enumerate(inorder):
            s[idx] = i
        mid = s[preorder[0]]

        left_size = mid

        left_preorder  = preorder[1 : 1 + left_size]
        right_preorder = preorder[1 + left_size: ]
        
        root.left = self.buildTree(left_preorder, inorder[:mid])
        root.right = self.buildTree(right_preorder, inorder[mid+1:])

        return root
