class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        def findPivot(nums: List[int], left: int, right: int) -> int:
            while left < right:
                mid = (left + right)//2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return left

        pivot = findPivot(nums, l, r)

        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1
        
        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1
            

