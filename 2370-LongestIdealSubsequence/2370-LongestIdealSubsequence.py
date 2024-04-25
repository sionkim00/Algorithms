            maxi = float("-inf") 

            left = max((idx - k), 0)
            right = min((idx + k), 26)

            for j in range(left, right + 1):
                maxi = max(maxi, dp[j])
            
            dp[idx] = maxi + 1
            idx = ord(cur) - ord('a')
            cur = s[i]
        for i in range(N-1, -1, -1):

"
