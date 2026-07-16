class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int n = matrix.length;
        for(int i = 0; i<n; i++){
            int l = 0;
            int r = matrix[0].length -1;
            
            while (l <= r){
                int m = (int)((l + r) / 2);
                if (matrix[i][m] > target){
                    r = m -1;
                }else if(matrix[i][m] < target){
                    l = m + 1;
                }else{
                    return true;
                }

            }
        }
        return false;
    }
}
