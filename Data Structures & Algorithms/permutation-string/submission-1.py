class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1

        #print(s1_map)

        i, j = 0, len(s1)
        while j <= len(s2):
            s2_map = {}
            #print(s2[i:j])
            for c in s2[i:j]:
                s2_map[c] = s2_map.get(c, 0) + 1
            if s2_map != s1_map:
                i += 1
                j += 1
            else:
                return True
        
        return False