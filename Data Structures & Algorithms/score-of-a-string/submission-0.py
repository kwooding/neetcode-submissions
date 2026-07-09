class Solution:
    def scoreOfString(self, s: str) -> int:
        
        l,r =0 ,1
        res = 0
        for c in range(len(s)-1):
            res += abs(ord(s[l]) - ord(s[r]))

            l = l + 1
            r = r + 1

        return res