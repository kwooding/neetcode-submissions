class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer,Integer> map = new HashMap<>();
        for (int n : nums){
            if(!map.containsKey(n)){
                map.put(n, 1);
            }else{
                int currCount = map.get(n);
                map.put(n, currCount + 1);
            }
        }
        return Collections.max(map.entrySet(), Map.Entry.comparingByValue()).getKey();
    }
}