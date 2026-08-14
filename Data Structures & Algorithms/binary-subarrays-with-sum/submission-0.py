class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            curr = nums[i]
            if curr == goal:
                res += 1
            for j in range(i+1,n):
                curr += nums[j]
                if curr == goal:
                    res += 1
                elif curr > goal:
                    break

        return res
                