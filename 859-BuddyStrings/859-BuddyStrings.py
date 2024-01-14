            return False

        sCounter = Counter(s)
        gCounter = Counter(goal)

        for key in sCounter:
            if sCounter[key] != gCounter[key]:
                return False
        
        if cnt == 0:
            sCounter = Counter(s)
            if max(sCounter.values()) < 2:
                return False

        return True
"
