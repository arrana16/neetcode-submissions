class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cMap = {}
        count = 0
        if len(s) == 0:
            return 0
        maxLen = 1
        r = 0
        l = 0
        while r < len(s):
            c=s[r]
            if c not in cMap:
                cMap[c] = r
                # print(l, r, maxLen)
            else:
                # print(c)
                l = max(cMap[c]+1, l)
                cMap[c] = r
            maxLen = max(maxLen, r-l+1)
            r+=1

        
        return maxLen

        