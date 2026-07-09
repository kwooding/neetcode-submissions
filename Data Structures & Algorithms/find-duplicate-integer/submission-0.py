class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = dict()
        for n in nums:
            if n not in check:
                check[n] = 0
            else:
                return n