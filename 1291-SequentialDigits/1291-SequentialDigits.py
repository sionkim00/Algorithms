        res = []
        lowDigits = len(str(low))
        highDigits = len(str(high))

        for digits in range(lowDigits, highDigits+1):
            for start in range(1,9):
                if start + digits > 10:
                    break
                num = start
                prev = start
                for i in range(digits - 1):
                    num = num * 10
                    prev += 1
                    num += prev
                if low <= num <= high:
                    res.append(num)
        return res
1
