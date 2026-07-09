class Solution:
    def climbStairs(self, n: int) -> int:
        res = []
        for i in range(1,n+1):
            if i == 1:
                res.append(1)
            elif i == 2:
                res.append(2)
            else:
                res.append(res[-1] + res[-2])
        
        return res[-1]