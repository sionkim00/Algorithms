class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        arr = [float("-inf")] + arr + [float("-inf")]
        stack = []

        for i, n in enumerate(arr):
            while stack and n < stack[-1][1]:
                j, m = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                res = (res + m * left * right) % (10 ** 9 + 7)
            stack.append((i,n))
        return res
[
[
