class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
    
        def getSum(n):
            total = 0
            for num in str(n):
                total += int(num) * int(num)
            return total
    
        while n not in seen:
            seen.add(n)
            n = getSum(n)
            if n == 1:
                return True
    
        return False