class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        areAllUppers = word[0].isupper()
        areAllLowers = not areAllUppers
        isOnlyFirstUpper = areAllUppers

        N = len(word)
        i = 1
        while (i < N) and (areAllUppers or areAllLowers or isOnlyFirstUpper):
            isLower = word[i].islower()
            areAllUppers = areAllUppers and isLower == False
            areAllLowers = areAllLowers and isLower
            isOnlyFirstUpper = isOnlyFirstUpper and isLower
            i += 1
        return areAllUppers or areAllLowers or isOnlyFirstUpper
