class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        orderTbl = {}
        for i, char in enumerate(order):
            orderTbl[char] = i

        for i in range(len(words) - 1):
            for j in range(len(words[i])):

                if j >= len(words[i + 1]):
                    return False

                if words[i][j] == words[i + 1][j]:
                    continue

                if orderTbl[words[i][j]] > orderTbl[words[i + 1][j]]:
                    return False

                # We can stop the comparing
                # if we found the evidence that words[i][j] < words[i + 1][j].
                # Because the problem wants to know the words are sorted by "lexicographical" order or not.
                # We don't need to compare all characters
                break
        return True
