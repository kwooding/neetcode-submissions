
class Solution {
    
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> s = new HashSet();
        for(int num : nums){
            boolean c = s.contains(num);
            if (c == true){
                return true;
            }
            s.add(num);
        }
        return false;
    }
}