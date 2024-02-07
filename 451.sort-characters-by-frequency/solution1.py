class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        keys = sorted(counts.keys(), key = lambda x: -counts[x])
        
        result = ""
        for key in keys:
            result += key * counts[key]
        return result