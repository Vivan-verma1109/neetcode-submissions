class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        q = deque([root])
        total = 0

        while q:
            node = q.popleft()

            if low <= node.val <= high:
                total += node.val

            if node.val > low and node.left:
                q.append(node.left)

            if node.val < high and node.right:
                q.append(node.right)

        return total