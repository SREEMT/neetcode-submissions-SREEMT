class Solution:
    def isValid(self, s: str) -> bool:
        close_check = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        open_stack = []

        for c in s:
            if c in close_check:
                if open_stack and open_stack[-1] == close_check[c]:
                    open_stack.pop()
                else:
                    return False
            else:
                open_stack.append(c)
        
        return True if not open_stack else False
                