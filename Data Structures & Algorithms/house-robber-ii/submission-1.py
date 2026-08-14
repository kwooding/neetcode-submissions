class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            prev, curr = 0, 0
            for money in houses:
                prev, curr = curr, max(curr, prev + money)
            return curr

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
        '''
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            if i == len(nums) - 1:
                dp[i] = max(dp[i-1], nums[i] + dp[1])
            else:
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[-1]
        '''