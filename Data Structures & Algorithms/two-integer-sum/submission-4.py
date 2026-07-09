class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = 0
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums:
                j = nums.index(diff)
                if i != j:
                    return sorted([i,j]) 

