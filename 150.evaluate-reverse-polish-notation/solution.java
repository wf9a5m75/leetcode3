class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        
        Map<String, BiFunction<Integer, Integer, Integer>> operators = new HashMap<>();
        operators.put("+", (a, b) -> { return a + b; });
        operators.put("-", (a, b) -> { return a - b; });
        operators.put("/", (a, b) -> { return a / b; });
        operators.put("*", (a, b) -> { return a * b; });
        
        Arrays.stream(tokens).forEach(token -> {
            if (operators.containsKey(token)) {
                int rhv = stack.pop();
                int lhv = stack.pop();
                BiFunction<Integer, Integer, Integer> expression = operators.get(token);
                int result = expression.apply(lhv, rhv);
                stack.push(result);
            } else {
                stack.push(Integer.parseInt(token));
            }
        });
        return stack.pop();
    }
}