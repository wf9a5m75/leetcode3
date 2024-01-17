class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> counts = new HashMap<>();
        Set<Integer> occurrences = new HashSet<>();
        
        for (int val : arr) {
            counts.put(val, counts.getOrDefault(val, 0) + 1);
        }
        
        for (Integer cnt : counts.values()) {
            if (occurrences.contains(cnt)) {
                return false;
            }
            occurrences.add(cnt);
        }
        return true;
    }
}