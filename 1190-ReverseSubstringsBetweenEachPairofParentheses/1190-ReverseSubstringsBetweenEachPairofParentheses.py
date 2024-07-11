                start = stack.pop()
                rev = s[i-1:start:-1]
                for j in range(start+1, i):
                    s[j] = rev[j-start-1]

        ans = []
        for c in s:
                stack.append(i)
            elif s[i] == ")":
            if not (c in "()"):
                ans.append(c)
        return "".join(ans)
"
