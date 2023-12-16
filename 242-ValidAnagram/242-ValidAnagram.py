        for c in t:
            if not (c in letters) or letters[c] == 0:
                return False
            letters[c] -= 1
        
        for c in letters:
            if letters[c] > 0:
        
                return False
"
