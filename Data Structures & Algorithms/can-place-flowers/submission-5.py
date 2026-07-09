class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        f = [0] + flowerbed + [0]
        for j in range(1,len(f)-1):
            if f[j-1] != 1 and f[j] == 0 and f[j+1] != 1:
                count = count + 1
                f[j] = 1
        
        return count >= n