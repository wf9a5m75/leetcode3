function isNumber(token: string): boolean {
  return /^-?[0-9]+$/.test(token);
}

const BASE_DECIMAL = 10;

function evalRPN(tokens: string[]): number {
  const stack: string[] = [];
  
  const number_of_tokens = tokens.length;
  for (const token of tokens) {
      stack.push(token);
      if (stack.length < 3 || isNumber(stack.at(-1))) {
          continue;
      }
      
      const operator = stack.pop()!;
      const right_hand_token = stack.pop()!;
      const left_hand_token = stack.pop()!;
      
      const result = calculate({
          left_hand_token,
          right_hand_token,
          operator,
      });
      
      stack.push(result);
  }
  
  return parseInt(stack[0], BASE_DECIMAL);
};

function calculate(params: Required<{
  left_hand_token: string;
  right_hand_token: string;
  operator: string;
}>): string {
  const left_hand_value = parseInt(params.left_hand_token, BASE_DECIMAL);
  const right_hand_value = parseInt(params.right_hand_token, BASE_DECIMAL);
  switch (params.operator) {
      case "+":
          return (left_hand_value + right_hand_value).toString();
      case "-":
          return (left_hand_value - right_hand_value).toString();
      case "*":
          return (left_hand_value * right_hand_value).toString();
      case "/":
          return (~~(left_hand_value / right_hand_value)).toString();
      default:
          throw new Error(`unknown operator: "${params.operator}"`);
  }
}