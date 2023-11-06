class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def bt(i, target, k, cur):
            if k == 0 and target == 0:
                res.append(cur.copy())
                return
            elif k <= 0 or target <= 0:
                return
            
            for j in range(i, 10):
                cur.append(j)
                bt(j+1, target - j, k - 1, cur)
                cur.pop()
        
        bt(1, n, k, [])
        return res