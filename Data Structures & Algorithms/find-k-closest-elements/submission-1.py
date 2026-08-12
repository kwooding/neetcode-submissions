class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pairs = [(abs(num - x), num) for num in arr]
        pairs.sort()
        closest = [num for dist,num in pairs[:k]]
        return sorted(closest)