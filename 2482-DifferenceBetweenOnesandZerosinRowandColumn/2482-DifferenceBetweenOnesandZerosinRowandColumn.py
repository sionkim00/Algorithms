                    rows[i] -= 1
                    cols[j] -= 1
                else:
                    rows[i] += 1
                    cols[j] += 1
        
        res = [[0] * M for _ in range(N)]
        print(rows, cols)
        for i in range(N):
            for j in range(M):
                res[i][j] = rows[i] + cols[j]
        return res
[
