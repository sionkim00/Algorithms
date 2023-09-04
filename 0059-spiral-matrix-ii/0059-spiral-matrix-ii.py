class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        cmin = 0
        rmin = 1
        cmax = n
        rmax = n
        res = [[0] * n for _ in range(n)]
        
        cnt = 1

        r = 0
        c = 0
        while cnt <= n*n:
            # right
            while c < cmax:
                res[r][c] = cnt
                cnt += 1
                c += 1
            c -= 1
            cnt -= 1
            cmax -= 1

            if cnt >= n * n:
                break

            # down
            while r < rmax:
                res[r][c] = cnt
                cnt += 1
                r += 1
            r -= 1
            cnt -= 1
            rmax -= 1

            if cnt >= n * n:
                break
            
            # left
            while c >= cmin:
                res[r][c] = cnt
                cnt += 1
                c -= 1
            
            c += 1
            cnt -= 1
            cmin += 1

            if cnt >= n * n:
                break

            # up
            while r >= rmin:
                res[r][c] = cnt
                cnt += 1
                r -= 1
            r += 1
            cnt -= 1
            rmin += 1

            if cnt >= n * n:
                break
        return res