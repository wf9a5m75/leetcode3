class Solution {
    public int lengthOfLongestSubstring(String s) {
        boolean[] window = new boolean[256];
        
        char[] chars = s.toCharArray();
        int longest = 0;
        int L = 0;
        int R = 0;
        while ((R < chars.length) && (L <= R)) {
            while ((R < chars.length) && (!window[chars[R]])) {
                window[chars[R]] = true;
                R++;
            }
            // System.out.println(String.format("R=%d,L=%d, ans=%d", R, L, R - L));
            longest = Math.max(longest, R - L);
            if (R == chars.length) {
                break;
            }
            
            while (window[chars[R]]) {
                window[chars[L]] = false;
                L++;
            }
        }
        
        return longest;
    }
}