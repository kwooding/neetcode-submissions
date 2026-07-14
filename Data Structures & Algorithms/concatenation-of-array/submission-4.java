class Solution {
    public int[] getConcatenation(int[] nums) {
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < 2; i++){
            for (int n : nums){
                ans.add(n);
            }
        }
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }
}