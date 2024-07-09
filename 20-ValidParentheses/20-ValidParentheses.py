            if c in "({[":
                stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] != kvp[c]:
                    return False
        for c in s:
                stack.pop()

        stack = []
        kvp = {")": "(", "]": "[", "}": "{"}

    def isValid(self, s: str) -> bool:
class Solution:
"
