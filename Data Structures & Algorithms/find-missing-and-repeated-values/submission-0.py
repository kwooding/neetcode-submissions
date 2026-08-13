class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        check = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                check.append(grid[i][j])

        nums = set(range(1, len(check) +  1))

        repeated = -1
        for n in check:
            if n in nums:
                nums.discard(n)
            else:
                repeated = n

        missing = nums.pop()
        return [repeated, missing]
        
            