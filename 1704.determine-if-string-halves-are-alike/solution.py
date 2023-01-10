class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        N = len(s)
        vols = 0
        for i in range(N >> 1):
            if (s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']):
                vols += 1
        for i in range(N >> 1, N):
            if (s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']):
                vols -= 1
        return vols == 0
