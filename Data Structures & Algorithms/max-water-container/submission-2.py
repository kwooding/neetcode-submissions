class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = 0
        height = 0
        volume = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            height = min(heights[l], heights[r])
            new_volume = height *(r-l)
            if new_volume > volume:
                volume = new_volume
            if heights[r] > heights[l]:
                l += 1
            elif heights[l] > heights[r]:
                r-=1
            else:
                r-=1
                
        
        return volume