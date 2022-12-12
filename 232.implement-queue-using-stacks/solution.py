class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.useStack1 = True


    def push(self, x: int) -> None:
        if (self.useStack1 == False):
            while(self.stack2):
                self.stack1.append(self.stack2.pop())

        self.stack1.append(x)
        self.useStack1 = True

    def pop(self) -> int:
        self.useStack1 = False
        while(self.stack1):
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


    def peek(self) -> int:
        self.useStack1 = False
        while(self.stack1):
            self.stack2.append(self.stack1.pop())
        return self.stack2[-1]


    def empty(self) -> bool:
        return (len(self.stack1) + len(self.stack2)) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
