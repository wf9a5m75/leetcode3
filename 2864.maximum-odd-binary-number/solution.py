class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        oneCnt = -1
        zeroCnt = 0
        for bitChar in s:
            oneCnt += 1 if bitChar == "1" else 0
            zeroCnt += 1 if bitChar == "0" else 0
        
        results = ["1" * oneCnt, "0" * zeroCnt, "1"]
        
        return "".join(results)