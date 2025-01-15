class MinStack:

    def __init__(self):
        self.minValues = [inf]
        self.values = [inf]
        
    def push(self, val: int) -> None:
        self.minValues.append(min(val, self.minValues[-1]))
        self.values.append(val)

    def pop(self) -> None:
        self.minValues.pop()
        self.values.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.minValues[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()