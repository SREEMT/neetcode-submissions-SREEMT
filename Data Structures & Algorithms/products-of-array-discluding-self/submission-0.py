class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # initalize arrays based on size of list
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        # set beggining of pref and end of suff to 1
        pref[0] = suff[n - 1] = 1

        # goees through the array and mutliplies using pref to build pref
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        
        # same thing but backwards for the suff array
        for i in range(n -2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]

        # now using both arrays you can create the result
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res

            