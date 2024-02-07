class Solution:
    def compare(self, a: tuple[int, str], b: tuple[int, str]) -> int:
        if (a[0] != b[0]):
            return b[0] - a[0]
        return ord(b[1]) - ord(a[1])
        
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        freqList = []
        for char, cnt in counts.items():
            freqList.append([cnt, char])
            
        freqList.sort(key = functools.cmp_to_key(self.compare))
        
        result = ""
        for cnt, char in freqList:
            result += char * cnt
        return result