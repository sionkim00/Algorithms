                    head = mid + 1
                else:
                    tail = mid - 1
            else:
                if target < nums[mid] or target > nums[tail]:
                    tail = mid - 1
                else:
                    head = mid + 1
        return -1
[
