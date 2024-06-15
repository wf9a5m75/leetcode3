class MinStack {
    private values: number[] = [Number.MAX_SAFE_INTEGER];
    private minValues: number[] = [Number.MAX_SAFE_INTEGER];

    push(val: number): void {
        const minValue = Math.min(this.minValues.at(-1), val);
        this.minValues.push(minValue);
        this.values.push(val);
    }

    pop(): void {
        this.minValues.pop();
        this.values.pop();
    }

    top(): number {
        return this.values.at(-1);
    }

    getMin(): number {
        return this.minValues.at(-1);
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */