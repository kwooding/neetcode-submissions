class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []


        for n in range(0,numRows):
            val = 1
            row = [1]
            for k in range(1,n+1):
                val = val * (n - k + 1) // k
                row.append(val)
            res.append(row)



        return res