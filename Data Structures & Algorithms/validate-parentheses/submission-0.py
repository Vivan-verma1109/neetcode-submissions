class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if not stack or stack[-1] != match[c]:
                    return False
                stack.pop()

        return len(stack) == 0