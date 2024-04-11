            s.pop()
            k -= 1
        if not s:
            return "0"
        for i in range(len(s)):
            if s[i] != 0:
                return "".join(map(str, map(int, s[i:])))
        while s and k > 0:

        return "0"
"
