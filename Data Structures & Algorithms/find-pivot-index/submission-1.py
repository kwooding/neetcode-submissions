class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for n in range(len(nums)):
            if sum(nums[:n]) == sum(nums[n+1:]):
                return n




        return -1