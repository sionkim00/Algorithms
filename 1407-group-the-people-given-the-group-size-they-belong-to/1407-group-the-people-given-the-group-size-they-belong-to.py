class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        sizes = defaultdict(list)
        N = len(groupSizes)
        ans = []

        for i in range(N):
            sizes[groupSizes[i]].append(i)

        for key in sizes:
            cnt = 0
            cur = []
            for i in range(len(sizes[key])):
                cur.append(sizes[key][i])
                cnt += 1

                if cnt == key:
                    ans.append(cur)
                    cnt = 0
                    cur = []
        
        return ans