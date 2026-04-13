class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i != j:
            x = nums[i] + nums[j]
            if x == target:
                return [i, j]
            if j == (i + 1):
                i = i + 1
                j = len(nums) - 1
            else:
                j = j - 1
        