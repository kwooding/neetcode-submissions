class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        streak = 0
        cur_streak =0 
        for n in nums:
            if n == 1:
                cur_streak += 1
            elif n == 0:
                cur_streak = 0
            if cur_streak > streak:
                streak = cur_streak
        
        return streak
