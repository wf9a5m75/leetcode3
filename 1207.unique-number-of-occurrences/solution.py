from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        occurrences = set()
        for cnt in counts.values():
            if (cnt in occurrences):
                return False
            occurrences.add(cnt)
        return True