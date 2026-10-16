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
                stack.pop()
        return len(stack) == 0