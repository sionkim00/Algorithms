class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        doms = list(dominoes)
        q = deque()

        for i in range(len(doms)):
            if doms[i] != ".":
                q.append((i, doms[i]))
        
        while q:
            i, dom = q.popleft()

            if dom == "L":
                if i > 0 and doms[i-1] == ".":
                    doms[i-1] = "L"
                    q.append((i-1, "L"))
            else:
                if i+1 < len(doms) and doms[i+1] == ".":
                    if i+2 < len(doms) and doms[i+2] == "L":
                        doms[i+1] = "."
                        q.popleft()
                    else:
                        doms[i+1] = "R"
                        q.append((i+1, "R"))
        return "".join(doms)
