class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s)

        # flip the string overall
        L = 0
        R = N - 1
        while (L < R):
            s[L], s[R] = s[R], s[L]
            L += 1
            R -= 1

        # flip character order in each word
        L = R = 0
        while (R < N):
            while (R < N) and (s[R] != " "):
                R += 1

            # flip
            nextR = R
            R -= 1
            while (L < R):
                s[L], s[R] = s[R], s[L]
                L += 1
                R -= 1

            L = R = nextR + 1
        
