class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            a,b = stones.pop(), stones.pop()

            if a == b:
                continue
            if a > b:
                stones.append(a-b)

        if len(stones) > 0:
            return stones[0]
        else:
            return 0