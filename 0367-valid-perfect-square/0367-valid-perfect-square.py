class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # log(n) solution
        head = 1
        tail = num-1

        if num == 1:
            return True

        while head <= tail:
            mid = ((head+tail) // 2)
            if mid * mid == num:
                return True
            if mid * mid >= num:
                tail = mid - 1
            else:
                head = mid + 1

        return False