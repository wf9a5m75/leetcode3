class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        size1 = M * N
        size2 = r * c

        if (size1 != size2) or ((M == r) and (N == c)):
            return mat

        mat2 = [[0] * c for _ in range(r)]
        dx = dy = 0
        for sy in range(M):
            for sx in range(N):
                mat2[dy][dx] = mat[sy][sx]

                dx += 1
                if dx == c:
                    dx = 0
                    dy += 1
        return mat2
