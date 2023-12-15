class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dest = defaultdict(list)

        for src, dst in paths:
            dest[src].append(dst)
        for src in dest:
            if len(dest[src]) == 0:
            if not dst in dest:
                dest[dst] = []


                return src
[
