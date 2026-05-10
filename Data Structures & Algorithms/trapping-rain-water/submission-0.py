class Solution:
    def trap(self, height: List[int]) -> int:
        pref = []
        suff = []
        l = 0
        r = len(height) - 1
        area = 0


        max_suff = 0
        max_pref = 0
        while l < len(height) and r >= 0:
            if max_pref < height[l]:
                max_pref = height[l]
                pref.append(max_pref)
            else:
                pref.append(max_pref)
            
            if max_suff < height[r]:
                max_suff = height[r]
                suff.insert(0, max_suff)
            else:
                suff.insert(0, max_suff)
            l += 1
            r -= 1

        for i in range(len(height)):
            area += min(pref[i], suff[i]) - height[i]
        
        return area