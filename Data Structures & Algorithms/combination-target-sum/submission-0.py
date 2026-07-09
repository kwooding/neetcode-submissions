class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        def dfs(i,currList,total):
            if total == target:
                self.res.append(currList[:])
                return
            if i >= len(nums) or total > target:
                return 
            
            currList.append(nums[i])
            dfs(i,currList,total + nums[i])
            currList.remove(nums[i])
            dfs(i+1,currList,total)


        dfs(0,[],0)

        return self.res