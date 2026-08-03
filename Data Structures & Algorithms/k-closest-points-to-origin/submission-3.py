class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pnts = {}
        for p in points:
            x = p[0]
            y = p[1]
            ed = math.sqrt(x**2 + y**2)
            pnts[tuple(p)] = ed
        sorted_points = sorted(pnts, key=lambda pt: pnts[pt])
        result = [list(pt) for pt in sorted_points[:k]]
        return result