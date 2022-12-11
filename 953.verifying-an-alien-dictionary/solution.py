class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        toOutEnglish = {}
        aChar = ord('a')
        for i, alieanChar in enumerate(order):
            toOutEnglish[alieanChar] = chr(i + aChar)

        # convert to our alphabet order
        words2 = []
        for word in words:
            word2 = ""
            for c in word:
                word2 += toOutEnglish[c]
            words2.append(word2)

        # sort
        words3 = sorted(words2)

        return words2 == words3

        
