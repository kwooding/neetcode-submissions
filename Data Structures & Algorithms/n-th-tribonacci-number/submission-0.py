class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 1 if n != 0 else 0
        base = [0] * (n+1)
        base[1] = base[2] = 1
        for i in range(3,n+1):
            base[i] = base[i-1] + base[i-2] + base[i-3]
        return base[n]