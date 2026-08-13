class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for n in range(len(nums)):
            d[nums[n]] = n
        
        for i in range(len(nums)):
            t = target - nums[i]
            if t in d and d[t] !=  i:
                return [i,d[t]]
        
        return []