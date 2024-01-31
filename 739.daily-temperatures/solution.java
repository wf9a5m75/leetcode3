class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> monoStack = new Stack<>();
        int N = temperatures.length;
        int[] results = new int[N];
        
        for (int i = 0; i < N; i++) {
            
            int today = temperatures[i];
            while (!monoStack.isEmpty() && temperatures[monoStack.peek()] < today) {
                
                // Represents the index of the day 
                // which is the lower temperature than today.
                int prevIdx = monoStack.pop();
                
                // Stores the duration
                results[prevIdx] = i - prevIdx;
            }
            
            monoStack.push(i);
        }
        
        return results;
    }
}