class Solution:
    def checkValidString(self, s: str) -> bool:
        N = len(s)
        memo = defaultdict()

        def dp(i=0, stack = []):
            key = (i, " ".join(stack))
            if key in memo:
                pass
            elif i == N:
                if stack:
                    memo[key] = False
                else:
                    memo[key] = True
            elif s[i] == '(':
                newArr = [*stack, '(']
                memo[key] = dp(i+1, newArr)
            elif s[i] == ')':
                newArr = [*stack]
                if len(newArr) == 0:
                    memo[key] = False
                else:
                    top = newArr.pop()
                    if top == "(":
                        memo[key] = dp(i+1, newArr)
                    else:
                        memo[key] = False
            else:
                res1 = dp(i+1, [*stack, '('])
                res3 = dp(i+1, stack)
                res2 = False

                if stack:
                    newArr = [*stack]
                    top = newArr.pop()
                    if top == '(':
                        res2 = dp(i+1, newArr)
                    else:
                        res2 = False

                memo[key] = res1 or res2 or res3
            return memo[key]
        return dp()