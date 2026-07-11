class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights) - 1
        res = 0
        while l < r:
            if heights[l] < heights[r]:
                curr = (heights[l] * (r-l))
                l = l + 1
            else:
                curr = (heights[r] * (r-l))
                r = r - 1
            
            
            if curr > res:
                res = curr


        return res