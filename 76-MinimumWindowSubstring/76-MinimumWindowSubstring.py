class Solution:
    def minWindow(self, s: str, t: str) -> str:
        kvpS = defaultdict(int) 
        kvpT = defaultdict(int)
        
        for c in t:
            kvpT[c] += 1
"
