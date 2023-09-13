class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        M = len(matrix[0])
        rows = set()
        cols = set()

        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(N):
            for j in range(M):
                if (i in rows) or (j in cols):
                    matrix[i][j] = 0
        print(matrix)