                for j in range(i+1, len(nums)):
                    if nums[j] % nums[i] == 0:
                        tmp = [nums[i]] + dp(j)
                        if len(tmp) > len(res):
                            res = tmp
            else:
                res = [nums[i]]
            elif i == len(nums):
                memo[i] = []
                memo[i] = res
            return memo[i]
        
        res = []
        for i in range(len(nums)):
            tmp = dp(i)
            if len(tmp) > len(res):
                res = tmp
        return res
[
