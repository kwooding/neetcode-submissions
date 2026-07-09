class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            if i == 0:
                res.append(0)
            if i == 1:
                res.append(1)   
            if i % 2 == 0 and i !=0:
                res.append(res[i >> 1])
            if i %2 != 0 and i != 1:
                res.append(res[(i - 1) >> 1] + 1)
            print(i)
            print(res)
            

        return res