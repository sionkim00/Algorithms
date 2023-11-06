class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        N = len(candidates)

        def bt(i, target, arr):
            if target == 0:
                res.append(arr.copy())
                return
            if target <= 0:
                return
            
            prev = -1
            for j in range(i, N):
                if candidates[j] == prev:
                    continue
                arr.append(candidates[j])
                bt(j+1, target-candidates[j], arr)
                arr.pop()
                prev = candidates[j]
        
        bt(0, target, [])

        return res