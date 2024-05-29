        for num in nums:
            if not(num-1) in s:
                length = 0
                while (length + num) in s:
                    length += 1
                maxLen = max(maxLen, length)
        return maxLen
[
