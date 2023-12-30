        kvp = defaultdict(int)
        N = len(words)

        for word in words:
            for c in word:
                kvp[c] += 1
        
        for key in kvp:
            if kvp[key] % N != 0:
                return False
        return True
[
