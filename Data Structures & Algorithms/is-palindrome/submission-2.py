class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum()).lower()
        print(s)
        
        i = 0
        j = len(s) - 1

        while i != j and i < j:
            print(i, j)
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True