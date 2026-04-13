class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        left = 0
        right = len(newStr) - 1

        while left < right:
            if newStr[left] != newStr[right]:
                return False
            left = left + 1
            right = right - 1
        return True
        