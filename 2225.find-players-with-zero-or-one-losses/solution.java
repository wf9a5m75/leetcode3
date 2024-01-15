class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        Map<Integer, Integer> lost = new HashMap<>();
        
        for (int[] match : matches) {
            lost.putIfAbsent(match[0], 0);
            lost.put(match[1], lost.getOrDefault(match[1], 0) + 1);
        }
        
        List<Integer> zero = lost.entrySet().stream()
            .filter(entry -> entry.getValue() == 0)
            .map(Map.Entry::getKey)
            .sorted()
            .collect(Collectors.toList());
        
        List<Integer> ones = lost.entrySet().stream()
            .filter(entry -> entry.getValue() == 1)
            .map(Map.Entry::getKey)
            .sorted()
            .collect(Collectors.toList());
        
        List<List<Integer>> results = new ArrayList<>();
        results.add(zero);
        results.add(ones);
        return results;
    }
}