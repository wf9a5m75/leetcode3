class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1) or (len(s) < numRows):
            return s
        rows = ["" for _ in range(numRows)]
        rowIdx = 0
        delta = 1

        for char in s:
            rows[rowIdx] += char
            rowIdx += delta
            if (rowIdx == 0) or (rowIdx == numRows - 1):
                delta *= -1

        result = ""
        for row in rows:
            result += row
        return result
