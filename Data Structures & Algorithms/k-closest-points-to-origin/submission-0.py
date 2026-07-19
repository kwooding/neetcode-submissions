class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        for p in points:
            dist = math.sqrt((p[0])**2 + (p[1])**2)
            ans.append([dist,p])

        ans.sort()

        return [p for dist, p in ans[:k]]