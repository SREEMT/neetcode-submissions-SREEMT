class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        dict_s = {}
        res = 0

        for r in range(len(s)):
            if s[r] in dict_s:
                l = max(dict_s[s[r]] + 1, l)
            dict_s[s[r]] = r
            res = max(res, r - l + 1)
        return res       