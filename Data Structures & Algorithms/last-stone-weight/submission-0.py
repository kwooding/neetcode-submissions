class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        
        while len(stones) > 1:
            
            stones.sort()
            l = len(stones)
            x = stones[-2]
            y = stones[-1]

            if x == y:
                stones = stones[0:(l-2)]
            if x < y:
                res = y - x
                stones = stones[0:(l-2)]
                stones.append(res)

        if stones:
            return stones[0]
        return 0