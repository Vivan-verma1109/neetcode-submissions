class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s) - 1
        while s[index] == " ":
            index -= 1
        print(s[index])
        count = 0
        while s[index] != " " and index >= 0:
            count += 1
            index -= 1
        return count