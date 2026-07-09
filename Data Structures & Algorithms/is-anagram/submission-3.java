class Solution {
    public boolean isAnagram(String s, String t) {
        char[] w1 = s.toCharArray();
        char[] w2 = t.toCharArray();

        java.util.Arrays.sort(w1);
        java.util.Arrays.sort(w2);

        
        return java.util.Arrays.equals(w1, w2);
    }
}
