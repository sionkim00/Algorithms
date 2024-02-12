        for num in nums:
            if cnt == 0:
                sol = num
            if num == sol:
                cnt += 1
            else:
                cnt -= 1
        return sol
[
