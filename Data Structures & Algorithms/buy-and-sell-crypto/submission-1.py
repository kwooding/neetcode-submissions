class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 9999999
        profit = 0
        for p in prices:
            if p < buy:
                buy = p
            elif p > buy:
                new_profit = p - buy
                if new_profit > profit:
                    profit = p - buy
            else:
                continue

        return profit