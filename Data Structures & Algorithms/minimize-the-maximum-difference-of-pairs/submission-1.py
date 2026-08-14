class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        lo,hi = 0 , nums[-1] - nums[0]

        def countPairs(d):
            count,i = 0,0
            while i < len(nums) - 1:
                if nums[i+1] - nums[i] <= d:
                    count += 1
                    i += 2
                else:
                    i += 1

            return count

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if countPairs(mid) >= p:
                hi = mid
            else:
                lo = mid + 1
        
        return lo