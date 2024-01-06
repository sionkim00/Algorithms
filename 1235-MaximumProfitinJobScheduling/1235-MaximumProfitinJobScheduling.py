                while j < N:
                # include

            else:
                # don't include
                memo[i] = dp(i+1)
                    if intervals[j][0] >= intervals[i][1]:
                        break
                j =bisect.bisect(intervals, (intervals[i][1], -1, 
-1))
[
