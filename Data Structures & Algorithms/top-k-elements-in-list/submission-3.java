class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap<>();
        for (int n: nums){
            if(!map.containsKey(n)){
                map.put(n,1);
            }else{
                int currCount = map.get(n);
                map.put(n,currCount+1);
            }
        }

        return map.keySet().stream()
                            .sorted((a, b) -> map.get(b) - map.get(a))
                            .limit(k)
                            .mapToInt(Integer::intValue)
                            .toArray();
    }
}
