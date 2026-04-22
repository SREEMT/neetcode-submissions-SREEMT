class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
        mon_stack = []
        
        left = [-1] * l         # Left boundries
        right = [l] * l         # Right boundries

        max_area = 0
        for i, curr_height in enumerate(heights):

            # Checks if current height 
            while mon_stack and heights[mon_stack[-1]] >= curr_height:
                right[mon_stack[-1]] = i
                mon_stack.pop()
            
            # teh remaining top of stack is the left bound of the current index
            if mon_stack:
                left[i] = mon_stack[-1]
            mon_stack.append(i)
        
        max_area = max(
            height * (right[i] - left[i] - 1)
            for i, height in enumerate(heights)
        )

        return max_area
            