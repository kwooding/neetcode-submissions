class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            pos = (low+high) // 2
            if nums[pos] == target:
                return pos           
            elif nums[pos] < target:
                low = low + 1
            else:
                high = high -1

        return -1