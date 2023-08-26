from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts = defaultdict(int)
        
        for sChar in s:
            counts[sChar] += 1
        
        for tChar in t:
            counts[tChar] -= 1
        
        for key in counts.keys():
            value = counts[key]
            # t の方が1文字多いと定義しているので、-1 になる
            if (value == -1):
                return key
        raise Exception("Something wrong!")