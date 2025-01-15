class Trie:

    def __init__(self):
        self.root = {"eow": False, "childs": {}}

    def insert(self, word: str) -> None:
        parent = self.root
        for char in word:
            if not (char in parent["childs"]):
                parent["childs"][char] = {"eow": False, "childs": {}}

            parent = parent["childs"][char]
        parent["eow"] = True

    def search(self, word: str) -> bool:
        parent = self.root
        for char in word:
            if not(char in parent["childs"]):
                return False
            parent = parent["childs"][char]
        return parent["eow"]
        
    def startsWith(self, prefix: str) -> bool:
        parent = self.root
        for char in prefix:
            if not(char in parent["childs"]):
                return False
            parent = parent["childs"][char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)