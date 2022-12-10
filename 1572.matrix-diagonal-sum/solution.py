class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        s1 = 0
        s2 = 0
        for i in range(N):
            s1 += mat[i][i]
            s2 += mat[i][N - i - 1] if i != N - i - 1 else 0
        return s1 + s2
