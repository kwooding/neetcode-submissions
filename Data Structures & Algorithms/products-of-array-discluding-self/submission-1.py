class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        n = len(nums)
        res = [1] * n
        pre = [1] * n
        suf = [1] * n

        for i in range(1,n):
            pre[i] = pre[i - 1] * nums[i -1]

        for i in range(n-2,-1,-1):
            suf[i] = suf[i+1] * nums[i+1]

        for i in range(n):
            res[i] = pre[i] * suf[i]

        

        return res


        '''
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) -1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
        
        
