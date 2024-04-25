            maxVal = float("-inf")

            left = max(0, charIdx - k)
            right = min(26, charIdx + k)

            for j in range(left, right + 1):
                maxVal = max(maxVal, dp[j])
            
            dp[charIdx] = maxVal + 1
        return max(dp)
"
