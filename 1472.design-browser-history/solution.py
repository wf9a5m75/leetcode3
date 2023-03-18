from dataclasses import dataclass

@dataclass
class ListNode:
    url: str = ""
    prev: ListNode = None
    next: ListNode = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)

    def visit(self, url: str) -> None:
        willDeleted = self.curr.next

        visit = ListNode(url)
        self.curr.next = visit
        visit.prev = self.curr
        self.curr = visit

        self._clearForward(willDeleted)

    def _clearForward(self, node: Optional[ListNode]):
        while (node):
            node2 = node.next
            node.prev = None
            node.next = None
            node = node2

    def back(self, steps: int) -> str:
        while (steps > 0) and (self.curr.prev):
            self.curr = self.curr.prev
            steps -= 1

        return self.curr.url

    def forward(self, steps: int) -> str:
        while (steps > 0) and (self.curr.next):
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
