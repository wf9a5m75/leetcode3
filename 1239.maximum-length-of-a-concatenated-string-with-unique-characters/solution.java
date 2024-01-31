class Solution {
    private Integer toInt(String s) {
        int result = 0;
        
        for (int i = 0; i < s.length(); i++) {
            int flag = 1 << (s.charAt(i) - 'a');
            // If same charactor in the s, such as "uu",
            // returns 0
            if ((result & flag) != 0) {
                return 0;
            }
            result |= flag;
        }
        return result;
    }
    
    public int maxLength(List<String> arr) {
        final Map<Integer, Integer> dp = new HashMap<>();
        arr.forEach(s -> {
            int sLen = s.length();
            
            // Generates bit flags
            int bitFlag = this.toInt(s);
            if (bitFlag == 0) {
                return;
            }
            
            Integer[] prevKeys = dp.keySet().toArray(new Integer[0]);
            Integer[] prevValues = dp.values().toArray(new Integer[0]);
            
            for (int i = 0; i < prevKeys.length; i++) {
                int prevFlag = prevKeys[i];
                int xorResult = prevFlag ^ bitFlag;
                int orResult = prevFlag | bitFlag;
                
                if (xorResult != orResult) {
                    continue;
                }
                dp.put(orResult, prevValues[i] + sLen);
            }
            
            // Adds doNothing case for the current s
            dp.put(bitFlag, sLen);
        });
        
        int longestS = 0;
        for (Integer count : dp.values()) {
            longestS = Math.max(longestS, count);
        }
        
        return longestS;
    }
}