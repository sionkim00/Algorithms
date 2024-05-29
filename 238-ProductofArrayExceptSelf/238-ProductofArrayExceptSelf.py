            if i == 0:
                res.append(rArr[i+1])
            elif i == N-1:
                res.append(lArr[i-1])
            else:
                res.append(lArr[i-1] * rArr[i+1])
        return res
[
