class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for e in arr2:
            for e2 in arr1:
                if e2 == e:
                    res.append(e2)
        
        res2 = []
        for e in arr1:
            if e not in res:
                res2.append(e)

        res2.sort()
        for e in res2:
            res.append(e)
        return res