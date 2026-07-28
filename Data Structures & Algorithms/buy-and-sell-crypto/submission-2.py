class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            max_i = 0
            for j in range(i+1,len(prices)):
                if prices[j] - prices[i] > max_i:
                    max_i = prices[j] - prices[i]

            if max_i > res:
                res = max_i

        return res