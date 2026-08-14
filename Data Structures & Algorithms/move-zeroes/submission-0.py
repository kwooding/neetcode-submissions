class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p,i =0,0
        while i < len(nums):
            if nums[i] == 0:
                i += 1
            else:
                temp = nums[p]
                nums[p] = nums[i]
                nums[i] = temp
                i += 1
                p +=1

        