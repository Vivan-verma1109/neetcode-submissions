class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        nums = [0] * len(s)

        for start, end, direction in shifts:
            for i in range(start, end + 1):
                if direction == 0:
                    nums[i] -= 1
                else:
                    nums[i] += 1

        res = ""

        for i in range(len(s)):
            new_char = (ord(s[i]) - ord('a') + nums[i]) % 26
            res += chr(new_char + ord('a'))

        return res