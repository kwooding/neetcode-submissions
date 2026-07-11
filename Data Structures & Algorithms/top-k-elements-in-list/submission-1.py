class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        
        for n in nums:
            if n not in res:
                res[n] = 1
            else:
                res[n] += 1

        top_k_keys = [item[0] for item in Counter(res).most_common(k)]

        return top_k_keys