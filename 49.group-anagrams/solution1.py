from collections import defaultdict

class Solution:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        buffer = defaultdict(list)
        ordA = ord("a")
        MOD = 10**9 + 7
        
        for word in words:
            
            hashKey = 1
            for char in word:
                hashKey = (hashKey * self.primes[ord(char) - ordA]) % MOD
            
            buffer[hashKey].append(word)
        
        return list(buffer.values())