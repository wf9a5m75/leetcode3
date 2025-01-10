function isValid(s: string): boolean {
  const stack: string[] = [];
  for (const char of s) {
      switch (char) {
          case "(":
              stack.push(")");
              continue;
          case "[":
              stack.push("]");
              continue;
          case "{":
              stack.push("}");
              continue;
          case ")":
          case "]":
          case "}":
              if (stack.length === 0 || stack.at(-1) !== char) {
                  return false;
              }
              stack.pop();
              continue;
          default:
              // Do nothing here;
              break;
      }
  }
  return stack.length === 0;
};