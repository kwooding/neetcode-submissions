class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for n in nums:
            if n not in res:
                res[n]  =1
            else:
                res[n] += 1

        print(res)

        return max(res,key=res.get)

