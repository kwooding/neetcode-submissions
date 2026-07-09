class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        comp = set(nums)
        if len(comp) == len(nums):
            return False
        else:
            return True