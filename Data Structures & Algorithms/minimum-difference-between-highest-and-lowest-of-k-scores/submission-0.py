class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        diff = 100000
        nums.sort()
        print(nums)
        l,r =0,k-1
        while r < len(nums):
           
            print(nums[l:r+1])
            print( nums[r])
            print(nums[l])
            check = nums[r] - nums[l]
            print(check)
            if check < diff:
                diff = check
            l = l + 1
            r = r + 1
            
        return diff
