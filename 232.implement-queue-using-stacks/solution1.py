from enum import Enum
Action = Enum("Action", ["push", "pop"])

class MyQueue:

    def __init__(self):
        self.__count = 0
        self.__idx = 0
        self.__stacks = [[], []]
        self.__lastAction = Action.push
        

    def push(self, x: int) -> None:
        if (self.__lastAction == Action.pop):
            self.flipStacks()
        self.__lastAction = Action.push
        self.__count += 1
            
        self.__stacks[self.__idx].append(x)
        
    def pop(self) -> int:
        if (self.__lastAction == Action.push):
            self.flipStacks()
        self.__lastAction = Action.pop
        self.__count -= 1
        return self.__stacks[self.__idx].pop()
        
    def peek(self) -> int:
        if (self.__lastAction == Action.push):
            self.flipStacks()
        self.__lastAction = Action.pop
        return self.__stacks[self.__idx][-1]

    def empty(self) -> bool:
        return self.__count == 0
    
    def flipStacks(self):
        sIdx = self.__idx
        dIdx = (self.__idx + 1) % 2
        while self.__stacks[sIdx]:
            self.__stacks[dIdx].append(self.__stacks[sIdx].pop())
        self.__idx = dIdx


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()