            if c in "{([":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top != p[c]:
                    return False
        return len(stack) == 0
"
"()"
"()[]{}"
"(]"
true
true
false
true
true
false
