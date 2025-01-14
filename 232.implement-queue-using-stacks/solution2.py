class MyQueue:

    def __init__(self):
        self.stacks = [[],[]]
        self.writeIdx = 0
        self.readIdx = 0

    def push(self, x: int) -> None:
        if self.readIdx != self.writeIdx:
            while self.stacks[self.writeIdx]:
                self.stacks[self.readIdx].append(self.stacks[self.writeIdx].pop())
            self.writeIdx = self.readIdx

        self.stacks[self.writeIdx].append(x)

    def pop(self) -> int:
        if self.readIdx == self.writeIdx:
            self.writeIdx = 1
            while self.stacks[self.readIdx]:
                self.stacks[self.writeIdx].append(self.stacks[self.readIdx].pop())
        
        return self.stacks[self.writeIdx].pop()
        
    def peek(self) -> int:
        if self.readIdx == self.writeIdx:
            return self.stacks[self.readIdx][0]
        else:
            return self.stacks[self.writeIdx][-1]
        
    def empty(self) -> bool:
        return len(self.stacks[self.readIdx]) == 0 and len(self.stacks[self.writeIdx]) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()