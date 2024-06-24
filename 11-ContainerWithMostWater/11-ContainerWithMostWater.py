        res = 0
        N = len(height)
        l, r = 0, N - 1

        while l < r:
            cur = min(height[l], height[r]) * (r-l)
            res = max(res, cur)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
[
