# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:


        def findSmallest(node):
            while node.left:
                node = node.left
            return node


        if not root:
            return None
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        
        if root.left and root.right:
            smallest = findSmallest(root.right)
            root.val = smallest.val
            root.right = self.deleteNode(root.right, smallest.val)
            return root
        if root.left:
            return root.left
        if root.right:
            return root.right
        return None