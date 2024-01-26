                return 0
            if x not in range(m) or y not in range(n):
                return 1
            if move > max_move:
            if (x, y, move) in memo:
                return memo[(x, y, move)] % mod
            memo[(x, y, move)] = solve(x, y - 1, move + 1) + solve(x - 1, y, move + 1) + \

        def solve(x: int, y: int, move: int) -> int:
        mod = 1000000007
                                 solve(x, y + 1, move + 1) + solve(x + 1, y, move + 1)
int:
        memo = {}
class Solution:
    def findPaths(self, m: int, n: int, max_move: int, start_row: int, start_col: int) -> 
2
