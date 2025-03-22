class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        n = len(currentState)
        if n == 1:
            return []
        
        results = []
        buff = ""
        for i in range(n - 1):
            if currentState[i] + currentState[i + 1] != "++":
                buff += currentState[i]
                continue
            results.append(f"{buff}--{currentState[i + 2:]}")
            buff += currentState[i]
        return results