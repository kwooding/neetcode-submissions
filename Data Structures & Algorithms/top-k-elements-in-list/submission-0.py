import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = list()
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        result = heapq.nlargest(k, d, key=lambda x: d[x])
        return result    