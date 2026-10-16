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
                if stack and stack[-1] not in match:
                    stack.pop()
        return len(stack) == 0