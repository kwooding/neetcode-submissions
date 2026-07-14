class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];
        for (int i = 0; i < nums.length; i++){
            int search = target - nums[i];
            for (int j = 0; j < nums.length; j++){
                if (i == j){
                    continue;
                }
                if (nums[j] == search){
                    ans[0] = i;
                    ans[1] = j;
                    return ans;
                }
            }
        }
        return new int[2];
    }
}
