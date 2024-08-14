            mid = (l + r) // 2
            
            if isBadVersion(mid):
                r = mid - 1
        while l <= r:
                minBad = min(minBad, mid)
            else:
                l = mid + 1
        return minBad
5
5
4
1
1
4
1
4
1
