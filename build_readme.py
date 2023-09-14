class ListNode:
    prev: ListNode = None
    next: ListNode = None
    value: int
    key: str
    
    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value
        
class LRUCache:

    keyToNode: dict[str, ListNode] = {}
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        
        # Since the leetcode test code reuse the LRUCache class instance,
        # we need to reset the dictionary every times.
        
        self.keyToNode = {}
        self.head = ListNode(key="guard", value = -1)
        self.tail = ListNode(key="guard", value = -1)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if (key not in self.keyToNode):
            return -1
        node = self.keyToNode[key]
        self._remove(node)
        self._add(node)
        return node.value
        
        

    def put(self, key: int, value: int) -> None:
        node = None
        if (key in self.keyToNode):
            node = self.keyToNode[key]
            node.value = value
            self._remove(node)
            del self.keyToNode[key]
            
        else:
            node = ListNode(
                key = key,
                value = value
            )
            
        self.keyToNode[key] = node
        self._add(node)
        
        if (len(self.keyToNode) > self.capacity):
            leastUsedNode = self.head.next
            self._remove(leastUsedNode)
            del self.keyToNode[leastUsedNode.key]
            
        
    def _remove(self, node: ListNode):
        """
        prev ←━┓ node ┏━━→ next
               ┗━━━━━━┛
        """
        prevNode = node.prev
        nextNode = node.next
        nextNode.prev = prevNode
        prevNode.next = nextNode
        
    def _add(self, node: ListNode):
        """
        tailPrev ←→ node ←→ tail
        """
        tailPrev = self.tail.prev
        tailPrev.next = node
        node.prev = tailPrev
        node.next = self.tail
        self.tail.prev = node
        
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)