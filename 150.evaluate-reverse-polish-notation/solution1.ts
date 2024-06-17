function toInt(num: number) {
  return ~~num;
};


function evalRPN(tokens: string[]): number {
  const BASE_DECIMAL = 10;
  
  const calculation_table = {
      "+": (left_hand_value: number, right_hand_value: number): number => {
          return (left_hand_value + right_hand_value);
      },
      "-": (left_hand_value: number, right_hand_value: number): number => {
          return (left_hand_value - right_hand_value);
      },
      "*": (left_hand_value: number, right_hand_value: number): number => {
          return (left_hand_value * right_hand_value);
      },
      "/": (left_hand_value: number, right_hand_value: number): number => {
          return toInt(left_hand_value / right_hand_value)
      },
  };

  const stack: number[] = [];
  for (const token of tokens) {
      if (!(token in calculation_table)) {
          stack.push(parseInt(token, BASE_DECIMAL));
          continue;
      }
      const right_hand_value = stack.pop()!;
      const left_hand_value = stack.pop()!;
      const result = calculation_table[token](left_hand_value, right_hand_value);
      stack.push(result);
  }
  return stack.pop()!;
};