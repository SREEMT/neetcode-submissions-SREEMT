class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordsOut = []
        wordsDict = {}
        for str in strs:
            x = "".join(sorted(str))
            if x in wordsDict:
                wordsDict[x].append(str)
            else:
                wordsDict[x] = [str]
        for y in wordsDict:
            wordsOut.append(wordsDict[y])
        return wordsOut
        