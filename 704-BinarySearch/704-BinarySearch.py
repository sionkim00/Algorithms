        while head <= tail:
            mid = (head + tail) // 2

            if nums[mid] > target:
                tail = mid - 1
            elif nums[mid] < target:
                head = mid + 1
            else:
                return mid
        return -1
[
[-1,0,3,5,9,12]
9
[-1,0,3,5,9,12]
2
4
-1
4
-1
