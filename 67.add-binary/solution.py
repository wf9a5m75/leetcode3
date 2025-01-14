class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        i = len(a) - 1
        j = len(b) - 1
        aVal = 0
        bVal = 0
        carryUp = 0
        while i >= 0 or j >= 0 or carryUp > 0:
            aVal = int(a[i]) if i >= 0 else 0
            bVal = int(b[j]) if j >= 0 else 0
            calc = aVal + bVal + carryUp
            result = f"{(calc % 2)}{result}"
            carryUp = int(calc / 2)
            j -= 1
            i -= 1
        return result
