class Solution {
    public boolean closeStrings(String word1, String word2) {
        if (word1.length() != word2.length()) {
            return false;
        }
        
        int[] freq1 = new int[26];
        int[] freq2 = new int[26];
        for (int i = 0; i < word1.length(); i++) {
            freq1[word1.charAt(i) - 'a']++;
            freq2[word2.charAt(i) - 'a']++;
        }
        
        Map<Integer, Integer> values1 = new HashMap<>();
        Map<Integer, Integer> values2 = new HashMap<>();
        for (int i = 0; i < 26; i++) {
            if (freq1[i] == 0 && freq2[i] == 0) {
                continue;
            }
            if (freq1[i] == 0 || freq2[i] == 0) {
                // System.out.println(i);
                // System.out.println(Arrays.toString(freq1));
                // System.out.println(Arrays.toString(freq2));
                return false;
            }
            
            values1.put(
                freq1[i],
                values1.getOrDefault(freq1[i], 0) + 1
            );
            values2.put(
                freq2[i],
                values2.getOrDefault(freq2[i], 0) + 1
            );
        }
        
        for (Map.Entry<Integer, Integer> entry : values1.entrySet()) {
            int frequency = entry.getKey();
            int value = entry.getValue();
            
            if (values2.containsKey(frequency) == false ||
               values2.get(frequency) != value) {
                return false;
            }
        }
        return true;
    }
}