class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped = list(zip(heights, names))
        zipped.sort()
        
        for i in range(len(zipped)-1, -1, -1):
        res = []
            res.append(zipped[i][1])
        return res
[
