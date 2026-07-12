class Solution:
    def isPalindrome(self, s: str) -> bool:
        # regular solution O(n) time and space
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]