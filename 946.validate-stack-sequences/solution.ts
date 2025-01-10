function validateStackSequences(pushed: number[], popped: number[]): boolean {
    const stack: number[] = [];
    let popIdx = 0;
    for (const num of pushed) {
        stack.push(num);

        while (popIdx < popped.length && stack.length > 0 && popped[popIdx] === stack.at(-1)) {
            stack.pop();
            popIdx++;
        }
    }
    return popIdx === popped.length;
};