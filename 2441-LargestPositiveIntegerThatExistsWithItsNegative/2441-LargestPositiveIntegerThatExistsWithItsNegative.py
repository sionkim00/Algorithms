        kvp = defaultdict()
        maxVal = -1

        for num in nums:
            kvp[num] = True
        
        for num in nums:
            if num > 0 and (num * -1) in kvp:
                maxVal = max(maxVal, num)
        
        return maxVal
[
