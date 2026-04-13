class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = len(nums) + 1
        buckets = []
        while l != 0:
            buckets.append([])
            l -= 1

        freqDict = {}
        for i in nums:
            if i in freqDict:
                freqDict[i] += 1
            else:
                freqDict[i] = 1
        for n in freqDict:
            y = freqDict[n]
            buckets[y].append(n)
        
        res = []
        i = len(buckets) - 1
        while i != 0:
            for val in buckets[i]:
                res.append(val)
                if len(res) == k:
                    return res
            i -= 1
        return res