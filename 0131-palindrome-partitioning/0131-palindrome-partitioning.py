class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        N = len(s)
        def bt(i=0, arr = []):
            if i == N:
                res.append(arr)
            else:
                for j in range(i, N):
                    s1 = s[i:j+1]
                    valid = s1 == s1[::-1]
                    if valid:
                        bt(j+1, [*arr, s1])
        bt()
        return res