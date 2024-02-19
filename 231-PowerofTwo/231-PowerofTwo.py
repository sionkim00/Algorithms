class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        while n > 1:
            n >>= 1
            if n % 2 != 0:
                return False
        return n == 1
1
