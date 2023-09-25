class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        kvp1 = defaultdict(int)
        kvp2 = defaultdict(int)
        for c in s:
            kvp1[c] += 1
        for c in t:
            kvp2[c] += 1

        for key in kvp2:
            if kvp2[key] != kvp1[key]:
                return key
        