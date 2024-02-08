class Solution {
    public char findTheDifference(String s, String t) {
        int[] appearred = new int[26];
        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();
        for (int i = 0; i < sChars.length; i++) {
            int idx = sChars[i] - 'a';
            appearred[idx]++;
        }
        for (int j = 0; j < tChars.length; j++) {
            int idx = tChars[j] - 'a';
            appearred[idx]--;
        }
        
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        for (int i = 0; i < 26; i++) {
            if (appearred[i] != 0) {
                return alphabet.charAt(i);
            }
        }
        return 'a';
    }
}