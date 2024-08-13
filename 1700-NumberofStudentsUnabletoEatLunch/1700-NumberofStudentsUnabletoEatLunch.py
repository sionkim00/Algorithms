        res = len(students)
        s = Counter(students)

        for sandwich in sandwiches:
            if s[sandwich] > 0:
                res -= 1
                s[sandwich] -= 1
            else:
                return res
        return res
[
[1,1,0,0]
[0,1,0,1]
[1,1,1,0,0,1]
[1,0,0,0,1,1]
0
3
0
3
