from collections import defaultdict

class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        buffer = defaultdict(list)
        ordA = ord("a")
        for word in words:
            
            frequencies = [0] * 26
            for char in word:
                frequencies[ord(char) - ordA] += 1
            
            key = ""
            for i in range(26):
                if (frequencies[i] == 0):
                    continue
                key += f"{i}:{frequencies[i]};"
            
            buffer[key].append(word)
        
        return list(buffer.values())