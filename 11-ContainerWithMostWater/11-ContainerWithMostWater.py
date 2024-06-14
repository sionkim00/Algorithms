        N = len(height)
        l, r = 0, N - 1
        maxArea = 0

        while l < r:
            maxArea = max(maxArea, area)
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
            area = min(height[l], height[r]) 
* (r-l)
        return maxArea
[
