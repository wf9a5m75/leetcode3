class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder strBuilder = new StringBuilder();
        int i = 0;
        int j = 0;
        int N = word1.length();
        int M = word2.length();
        while ((i < N) || (j < M)) {
            if (i < N) {
                strBuilder.append(word1.charAt(i));
                i++;
            }
            if (j < M) {
                strBuilder.append(word2.charAt(j));
                j++;
            }
        }
        return strBuilder.toString();
    }
}