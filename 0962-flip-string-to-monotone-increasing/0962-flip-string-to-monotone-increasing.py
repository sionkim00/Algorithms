class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        N = len(s)
        memo = {}

        def dp(i, prev):
            key = (i, prev)
            if key in memo:
                pass
            elif i == N:
                memo[key] = 0
            else:
                cur = int(s[i])
                if prev == None:
                    if cur == 0:
                        memo[key] = min(dp(i+1, 0), dp(i+1, 1)+1)
                    else:
                        memo[key] = min(dp(i+1, 1), dp(i+1, 0)+1)
                else:
                    if prev == 0:
                        if cur == 0:
                            memo[key] = min(dp(i+1, 0), dp(i+1, 1)+1)
                        else:
                            memo[key] = min(dp(i+1, 0)+1, dp(i+1, 1))
                    else:
                        if cur == 0:
                            memo[key] = dp(i+1, 1)+1
                        else:
                            memo[key] = dp(i+1, 1)
            return memo[key]


        return dp(i=0, prev = None)