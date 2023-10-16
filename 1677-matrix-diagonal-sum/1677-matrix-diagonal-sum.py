class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        total = 0
        for i in range(N):
            total += mat[i][i]
        for i in range(N):
            total += mat[i][N-i-1]
        if N % 2 != 0:
            total -= mat[math.floor(N/2)][math.floor(N/2)]
        return total