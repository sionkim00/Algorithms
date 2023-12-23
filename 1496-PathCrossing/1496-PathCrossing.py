            if c == "N":
                y -= 1
            if c == "S":
                y += 1
            if c == "W":
                x -= 1
            if c == "E":
                x += 1
            
            if (x,y) in visited:
                return True
            visited.add((x,y))
        return False

        for c in path:
"
-
