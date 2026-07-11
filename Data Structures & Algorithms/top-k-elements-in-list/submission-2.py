class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums)

        top_k_keys = [item[0] for item in Counter(res).most_common(k)]

        return top_k_keys