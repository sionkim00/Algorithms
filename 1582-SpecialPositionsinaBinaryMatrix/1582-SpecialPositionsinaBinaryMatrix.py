        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if len(rows[i]) == 1 and len(cols[j]) == 1 and mat
[i][j] == 1:
                    cnt += 1
        print(rows, cols)
        return cnt
[
