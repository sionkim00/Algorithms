class Solution:
    def isUgly(self, n: int) -> bool:
        arr = [2,3,5]
        memo = {}
        if n <= 0:
            return False
        def check(n):
            if n in memo:
                pass
            else:
                if n == 1:
                    return True
                flag = False
                for e in arr:
                    if n % e == 0:
                        flag = flag or check(n/e)
                memo[n] = flag
            return memo[n]
        return check(n)
