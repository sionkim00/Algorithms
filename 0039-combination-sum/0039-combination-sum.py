class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def bt(i, cur, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target <= 0:
                return
            
            for j in range(i, len(candidates)):
                cur.append(candidates[j])
                bt(j, cur, target - candidates[j])
                cur.pop()
        
        bt(0,[],target)
        return res