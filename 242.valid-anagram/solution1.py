class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        sList = list(s)
        tList = list(t)
        sList.sort()
        tList.sort()
        for i in range(len(s)):
            if (sList[i] != tList[i]):
                return False
        return True