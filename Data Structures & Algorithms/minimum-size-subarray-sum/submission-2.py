class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        if sum(nums) < target:
            return 0
        for i in range(len(nums)):
            t = target - nums[i]
            if t <= 0:
                res = min(res, 1)
                continue

            for j in range(i+1,len(nums)):
                t = t - nums[j]
                if t <= 0:
                    res = min(res,j-i + 1)
                    break
        return res