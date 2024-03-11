class Solution:
    def customSortString(self, order: str, s: str) -> str:
        priority = [-1] * 26
        aOrd = ord('a')
        for i, char in enumerate(order):
            priority[ord(char) - aOrd] = i
        
        charList = list(s)
        charList.sort(key = lambda char: priority[ord(char) - aOrd])
        return "".join(charList)