                top_left = sub_matrix[r-1][c-1] if min(r,c) > 0 else 0
                sub_matrix[r][c] = matrix[r][c] + top + left - top_left
        
        res = 0
        for r1 in range(N):
            for r2 in range(r1, N):
                for c in range(M):

                left = sub_matrix[r][c-1] if c > 0 else 0
                count = defaultdict(int)
                count[0] = 1
                    cur_sum = sub_matrix[r2][c] - (sub_matrix[r1-1][c] if r1 > 0 else 0)
                    diff = cur_sum - target
                    res += count[diff]
                    count[cur_sum] += 1
        return res
[
