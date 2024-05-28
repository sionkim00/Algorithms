List[int]:
        kvp = defaultdict()

        for i in range(len(nums)):
            a = (target - nums[i])
            if a in kvp:
                return [kvp[a], i]
            kvp[nums[i]] = i
        

[
