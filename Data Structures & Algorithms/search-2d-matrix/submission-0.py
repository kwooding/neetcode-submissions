class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            l,r= 0,len(matrix[i]) - 1
            mid = (l + r) // 2
            while l <= r:
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
                mid = (l+r) // 2



        return False