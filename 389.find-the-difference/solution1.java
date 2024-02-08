class Solution {
    public char findTheDifference(String s, String t) {
        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();
        
        char ans = 0;
        for (char sChar : sChars) {
            ans ^= sChar;
        }
        for (char tChar : tChars) {
            ans ^= tChar;
        }
        
        return ans;
    }
}