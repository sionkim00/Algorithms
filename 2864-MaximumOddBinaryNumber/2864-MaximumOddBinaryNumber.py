class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        onesCnt = 0

        for c in s:
            if c == "1":
                onesCnt += 1
        
        if onesCnt >= 1:
            return "1" * (onesCnt-1) + "0" * (len(s)-onesCnt) + "1"
        else:
            return s
"
