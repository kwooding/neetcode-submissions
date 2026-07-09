class Solution:
    def maxDifference(self, s: str) -> int:
        res = {}
        for c in s:
            if c not in res:
                res[c] = 1
            else:
                res[c] += 1

        
        high = max(v for v in res.values() if v % 2 != 0)
        low = min(v for v in res.values() if v % 2 == 0)
        return high - low