            if not (lose in loseCount):
                loseCount[lose] = 0
            loseCount[lose] += 1
        
        ans1 = []
        ans2 = []
        for key in loseCount:
            if loseCount[key] == 0:
                ans1.append(key)
                loseCount[win] = 0
[
