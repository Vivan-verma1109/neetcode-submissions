# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        q = deque([root])
        res = []

        while q:
            level = []
            l = len(q)

            for _ in range(l):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            res.append(level)
        flat = [x for row in res for x in row]
        flat.sort()
        print(flat)
        return flat[k - 1]


