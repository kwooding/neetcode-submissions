class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_val = float('inf')

        for n in prices:
            min_val = min(min_val,n)
            res = max(res, n - min_val)

        return res