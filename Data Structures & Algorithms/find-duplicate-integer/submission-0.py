class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dupes = {}
        for i, n in enumerate(nums):
            dupes[n] = 1 + dupes.get(n, 0)
        
        for key, val in dupes.items():
            if val > 1:
                return key

        return
        