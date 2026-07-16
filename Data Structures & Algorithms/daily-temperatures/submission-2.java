class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] res = new int[n];
        for(int i = 0; i < n-1; i++){
            int key = temperatures[i];
            
            for(int j = i + 1; j < n; j++){
                if (temperatures[j] > key){
                    res[i] = (j-i);
                    break;
                }
            }
        }
        return res;
    }
}
