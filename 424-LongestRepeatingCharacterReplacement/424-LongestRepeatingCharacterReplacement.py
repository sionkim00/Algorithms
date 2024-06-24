
        for r in range(len(s)):
            kvp[s[r]] = 1 + kvp.get(s[r], 0)

            while (r-l+1) - max(kvp.values()) > k:
                kvp[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)

        return res
"
