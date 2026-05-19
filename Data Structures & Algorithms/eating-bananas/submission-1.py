class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return

        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            print(k)
            totalTime = 0

            for p in piles:
                totalTime += math.ceil(float(p)/k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
