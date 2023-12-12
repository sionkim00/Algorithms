        for i in range(0, N):
            if reachable >= N-1 or i > reachable:
                break
            reachable = max(reachable, i + nums[i])

        return reachable >= N-1

        N = len(nums)
        reachable = 0
[
