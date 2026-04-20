class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                top = stack.pop()
                res[top] = i - top
            stack.append(i)
        return res