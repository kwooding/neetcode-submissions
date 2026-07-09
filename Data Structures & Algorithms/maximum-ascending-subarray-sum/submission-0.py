class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        streak = 0
        curr = 0
        for i in range(len(nums)):
            if streak == 0:
                curr += nums[i]
                streak += 1
            
            else:
                if nums[i] > nums[i-1]:
                    streak += 1
                    curr += nums[i]
                else:
                    streak = 1
                    curr = nums[i]
            
            if curr > res:
                res = curr

        return res