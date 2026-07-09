class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for d in details:
            if int(d[11]) >= 6:
                if int(d[11]) == 6:
                    if int(d[12]) > 0:
                        res += 1
                else:
                    res += 1

        return res