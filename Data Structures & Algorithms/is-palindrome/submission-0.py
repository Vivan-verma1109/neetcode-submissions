class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""

        for ch in s.lower():
            if ch.isalnum():
                string += ch

        return string == string[::-1]