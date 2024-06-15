function isValid(s: string): boolean {
    const stack: string[] = [];
    const pairs = {
        "}": "{",
        ")": "(",
        "]": "[",
    };
    for (const char of s) {
        if (!(char in pairs)) {
            stack.push(char);
            continue;
        }
        const top = stack.pop()!;
        if (top !== pairs[char]) {
            return false;
        }
    }
    return stack.length === 0;
};