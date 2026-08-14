class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current = ""
        current_num = 0

        for i in s:
            if i.isdigit():
                current_num = current_num * 10 + int(i)

            elif i == "[":
                stack.append((current_num, current))
                current_num = 0
                current = ""
            elif i == "]":
                num, prev = stack.pop()
                current = prev + num * current
            else:
                current += i
        return current
