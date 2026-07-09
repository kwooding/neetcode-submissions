class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest_i = 1
        curr = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                curr += 1
            else:
                curr = 1
            longest_i = max(curr,longest_i)

             
        longest_d = 1
        curr = 1
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                curr += 1
            else:
                curr = 1
            longest_d = max(curr,longest_d)
        

        return max(longest_i, longest_d)