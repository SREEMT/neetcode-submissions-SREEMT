class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+', '-', '*', '/']

        def pol_math(t: str, l: int, r: int, stack: List[int]) -> List[int]:
            if t == '+':
                stack.append(l + r)
            elif t == '-':
                stack.append(l - r)
            elif t == '*':
                stack.append(l * r)
            elif t == '/':
                stack.append(int(l / r))
            return stack

        res = 0
        for t in tokens:
            if t not in operands:
                t = int(t)
                stack.append(t)
            else:
                right = stack.pop()
                left = stack.pop()

                stack = pol_math(t, left, right, stack)

        return stack.pop()
                