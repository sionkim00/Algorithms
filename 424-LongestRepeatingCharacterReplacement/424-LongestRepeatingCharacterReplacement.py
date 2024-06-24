        maxf = 0

        for r in range(len(s)):
            kvp[s[r]] = 1 + kvp.get(s[r], 0)
        kvp = {}
        l = 0
            maxf = max(maxf, kvp[s[r]])

            if (r-l+1) - maxf > k:
                kvp[s[l]] -= 1
                l += 1

"
